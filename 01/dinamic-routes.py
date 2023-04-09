#commands to run the app:
# * export FLASK_APP=filename.py
# * flask run
# * export FLASK_DEBUG=1

from flask import Flask

app = Flask(__name__) ##built in var that can be accessed by any file

@app.route("/") ##declarator

def hello_world():
    return "<p>TEST, World!</p>"

@app.route('/about/<username>')
def about_page(username):
    return f'<h1>this is a page of {username}</h1>'