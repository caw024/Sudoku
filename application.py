import random

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    # {{headline}} in the html is templating language called jinja2
    # flask uses this in html templates
    # debug mode on flask lets you live update your flask 
    headline = random.choice(["Hello, world!", "Hi there!", "Good morning!"])
    return render_template("index.html", headline=headline)
