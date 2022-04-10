from contextlib import contextmanager
from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)


@app.route("/")
@app.route("/<context>")
def index(context=None):
    if context is None:
        return render_template("index.html")
    return render_template("index.html", context=context)

@app.route("/post", methods=["POST"])
def post():
    context = request.form.get("name")
    return redirect(url_for("index", context=context))

@app.route("/login")
def login():
    return render_template("login.html")

    
if __name__ == "__main__":
    app.run(debug=True)