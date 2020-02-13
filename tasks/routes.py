from tasks import app
from flask import render_template

@app.route("/")
def index():
    return render_template("task.html")


@app.route("/salvarTarea")
def salvartarea():
    