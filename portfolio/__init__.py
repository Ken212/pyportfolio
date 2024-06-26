from flask import Flask, render_template, abort

app = Flask(__name__)

projects = [
    {
        "name": "Multi-User Chat Room with Python and Sockets",
        "thumb": "img/chat-room.jpg",
        "hero": "img/chat-room-ero.jpg",
        "categories": ["python", "networking"],
        "slug": "chat-room",
        "prod": "https://github.com/Ken212/chat-room-application.git",
    },
    {
        "name": "PDF Audio Reader",
        "thumb": "img/audio-reader.jpg",
        "hero": "img/audio-reader-ero.jpg",
        "categories": ["python", "web"],
        "slug": "audio-reader",
        "prod": "https://github.com/Ken212/pdf-audio-reader.git",
    },
    {
        "name": "PyMail: Python Email Client",
        "thumb": "img/auto-email-sender.jpg",
        "hero": "img/auto-email-sender-ero.jpg",
        "categories": ["python", "web"],
        "slug": "auto-email-sender",
        "prod": "https://github.com/Ken212/auto-email-sender.git",
    },
]

slug_to_project = {project["slug"]: project for project in projects}


@app.route("/")
def home():
    return render_template("home.html", projects=projects)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/project/<string:slug>")
def project(slug):
    if slug not in slug_to_project:
        abort(404) 
    return render_template(
        f"project_{slug}.html", 
        project=slug_to_project[slug]
        )


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404




