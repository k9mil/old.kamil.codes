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
    projects_list = [
        ["🗺️ statum", "A Twitch streamer-related website. Written in Python + Flask, with MongoDB. Current features include Twitch OAuth integration, personalized dashboard, unique streamer insights & much more."],
        ["🦅 eagle", "A simple, fast, and fun CLI-based application which functions as a helper to find answers to your programming questions!"],
        ["👁️ Oculus", "Unmaintained camera scraper for Allegro & OLX to try and catch low priced cameras at user-set prices."],
        ["⚡ kamil.codes", "My personal web(site) created with Flask, TailwindCSS and nginx."],
    ]
    return render_template("projects.html")

@main.route("/technologies")
def technologies():
    return render_template("technologies.html")

@main.route("/blog")
def blog():
    return render_template("blog.html")