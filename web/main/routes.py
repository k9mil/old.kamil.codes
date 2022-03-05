from flask import Blueprint, render_template, send_from_directory, request, current_app as app
import json, os

main = Blueprint('main', __name__)

@main.route("/")
def index():
    return render_template("index.html")

@main.route("/about")
def about():
    filename = os.path.join(app.static_folder, 'json/about.json')
    with open(filename) as about:
        data = json.load(about)

    return render_template("about.html", data=data)

@main.route("/projects")
def projects():
    projects_list = [
        ["🗺️ statum", "A Twitch streamer-related website. Written in Python + Flask, with MongoDB. Current features include Twitch OAuth integration, personalized dashboard, unique streamer insights & much more.", "https://github.com/k9mil/statum"],
        ["🦅 eagle", "A simple, fast, and fun CLI-based application which functions as a helper to find answers to your programming questions! Written in Golang + Cobra.", "https://github.com/k9mil/eagle"],
        ["⚡ kamil.codes", "My personal web(site) created with Flask, TailwindCSS and gunicorn.", "https://github.com/kamil-codes/kamil.codes"],
        ["👁️ Oculus", "Unmaintained camera scraper for Allegro & OLX to try and catch low priced cameras at user-set prices. Written in Python incl. BeautifulSoup4 & requests.", "https://github.com/k9mil/oculus-monitor"],
    ]

    return render_template("projects.html", projects=projects_list)

@main.route("/technologies")
def technologies():
    filename = os.path.join(app.static_folder, 'json/technologies.json')
    with open(filename) as technologies:
        data = json.load(technologies)

    return render_template("technologies.html", data=data)

@main.route("/blog")
def blog():
    return render_template("blog.html")

@main.route("/blog/oauth-twitch")
def oauth_twitch():
    return render_template("oauth_twitch.html")

@main.route("/robots.txt")
def robots_dot_txt():
    return send_from_directory(app.static_folder, request.path[1:])