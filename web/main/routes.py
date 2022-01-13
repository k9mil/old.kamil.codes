from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route("/")
def index():
    return render_template("index.html")

@main.route("/about")
def about():
    return render_template("about.html")

@main.route("/projects")
def projects():
    return render_template("projects.html")

@main.route("/technologies")
def technologies():
    return render_template("technologies.html")

@main.route("/blog")
def blog():
    return render_template("blog.html")