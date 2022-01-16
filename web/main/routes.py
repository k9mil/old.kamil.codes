from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route("/")
def index():
    return render_template("index.html")

@main.route("/about")
def about():
    film_list = [
        ['/static//img/film/taxi_driver.jpg', 'Taxi Driver'],
        ['/static//img/film/good_fellas.jpg', 'Goodfellas'],
        ['/static//img/film/fight_club.jpg', 'Fight Club'],
        ['/static//img/film/barry_lyndon.jpg', 'Barry Lyndon'],
        ['/static//img/film/children_of_men.jpg', 'Children of Men'],
        ['/static//img/film/la_haine.jpg', 'La Haine'],
    ]

    album_list = [
        ["/static//img/albums/mbdtf.jpg", "My Beautiful Dark Twisted Fantasy"],
        ["/static//img/albums/madvillain.jpg", "Madvillain"],
        ["/static//img/albums/atrocity_exhibition.jpg", "Atrocity Exhibition"],
        ["/static//img/albums/slauson_malone.jpg", "Vergangenheitsbewältigung"],
        ["/static//img/albums/blonde.jpg", "Blonde"],
        ["/static//img/albums/808s.jpg", "808s & Heartbreak"],
    ]

    book_list = [
        ["/static//img/book/1984.jpg", "1984"],
        ["/static//img/book/howtohidee.jpg", "How to Hide an Empire"],
        ["/static//img/book/sapiens.jpg", "Sapiens"],
        ["/static//img/book/steve_jobs.jpg", "Steve Jobs"],
        ["/static//img/book/technological_slavery.jpg", "Technological Slavery"],
        ["/static//img/book/bravenewworld.jpg", "Brave New World"],
    ]

    return render_template("about.html", films=film_list, albums=album_list, books=book_list)

@main.route("/projects")
def projects():
    projects_list = [
        ["🗺️ statum", "A Twitch streamer-related website. Written in Python + Flask, with MongoDB. Current features include Twitch OAuth integration, personalized dashboard, unique streamer insights & much more.", "https://github.com/k9mil/statum"],
        ["🦅 eagle", "A simple, fast, and fun CLI-based application which functions as a helper to find answers to your programming questions!", "https://github.com/k9mil/eagle"],
        ["👁️ Oculus", "Unmaintained camera scraper for Allegro & OLX to try and catch low priced cameras at user-set prices.", "https://github.com/k9mil/oculus-monitor"],
        ["⚡ kamil.codes", "My personal web(site) created with Flask, TailwindCSS and gunicorn.", "https://github.com/kamil-codes/kamil.codes"],
    ]

    return render_template("projects.html", projects=projects_list)

@main.route("/technologies")
def technologies():
    return render_template("technologies.html")

@main.route("/blog")
def blog():
    return render_template("blog.html")