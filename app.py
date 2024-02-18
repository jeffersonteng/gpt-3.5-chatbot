import collections
import os
import sqlite3

from flask import Flask, render_template, request, url_for, flash, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = '3d1d11bc16ae475be87bfaecf9cfc4bf39aa64c49ff3a303'

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/', methods=('GET', 'POST'))
def index():
    conn = get_db_connection()
    if request.method == 'GET':
        posts = conn.execute('SELECT * FROM posts').fetchall()
        print(posts)
        conn.close()
        return render_template('index.html', posts=posts)
    else:
        content = request.form['content']

        if not content:
            flash('Content is required!')
        else:
            conn = get_db_connection()
            print('gets here')
            conn.execute('INSERT INTO posts (content) VALUES (?)',
                         (content,))
            conn.commit()
            conn.close()
            return redirect(url_for('index')) 

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))