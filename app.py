import os
from flask import Flask, render_template
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


'''
safe -  passes html in render template
capitalize - first letter of the tag is capital
lower - whole tag is lower
upper - whole tag is capital
title - First letter of every word is uppercase
trim
striptags - ignores html in render template
'''

@app.route("/")


@app.route('/index')

def index():
    first_name = "John"
    stuff = "This is bold text"
    player = ["Messi", "Ronaldo", "Lewandowski", 5]
    return render_template("index.html", first_name = first_name, stuff = stuff, player = player)


@app.route('/user/<name>')

def user(name):
    return render_template("user.html", user_name = name)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)