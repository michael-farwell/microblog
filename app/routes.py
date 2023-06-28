from flask import render_template

from app import app


@app.route("/")
@app.route("/index")
def index():
    user = {"username": "Michael"}
    posts = [
        {
            "author": {"username": "Bilbo"},
            "body": "I'm going on an adventure!"
        },
        {
            "author": {"username": "Gandalf"},
            "body": "I have no memory of this place..."
        }
    ]
    return render_template("index.html",
                           title="Home",
                           user=user,
                           posts=posts)
