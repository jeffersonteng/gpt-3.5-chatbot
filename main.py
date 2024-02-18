import os

from flask import Flask, render_template

app = Flask(__name__)

messages = [
    {
    'title': 'Message One',
    'content': 'Message One Content'
    },
    {
    'title': 'Message Two',
    'content': 'Message Two Content'
    }
]


@app.route('/')
def index():
    return render_template('index.html', messages=messages)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))