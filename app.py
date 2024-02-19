import collections
import os
import sqlite3
from openai import OpenAI

from flask import Flask, render_template, request, url_for, flash, redirect

app = Flask(__name__, static_folder="static/")
app.config['SECRET_KEY'] = '3d1d11bc16ae475be87bfaecf9cfc4bf39aa64c49ff3a303'
client = OpenAI(api_key=os.environ['OPEN_AI'])

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_completion(prompt, model="gpt-3.5-turbo"):
  message = {"role": "user", "content": prompt}
  response = client.chat.completions.create(
      model=model,
      messages=[message]
  )
  return response.choices[0].message.content

def get_conversation():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    convo = ""
    for post in posts:
        convo += "\n" + post['content']
    conn.close()
    return convo

@app.route('/', methods=('GET', 'POST'))
def index():
    conn = get_db_connection()
    if request.method == 'GET':
        posts = conn.execute('SELECT * FROM posts').fetchall()
        conn.close()
        return render_template('index.html', posts=posts)
    else:
        context = get_conversation()
        input = request.form['content']
        query = ""
        if context != "":
            query = 'The conversation history is between two triple backticks. ```' + context + '```\n'
            query += 'With the above conversation history, answer the following question: '
        query += input
        response = get_completion(query)

        if not input:
            flash('Content is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO posts (content, role) VALUES (?, ?)',
                         (input,'user'))
            conn.execute('INSERT INTO posts (content, role) VALUES (?, ?)',
                         (response,'gpt'))
            conn.commit()
            conn.close()
            return redirect(url_for('index')) 

@app.route('/reset', methods=(['GET', 'POST']))
def reset():
    file = open(r'init_db.py', 'r').read()
    exec(file)
    return redirect(url_for('index')) 

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))