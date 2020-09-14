import random
import getRandomPuzzle from request
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    # {{headline}} in the html is templating language called jinja2
    # flask uses this in html templates
    # debug mode on flask lets you live update your flask 
    puzzle = getRandomPuzzle()
    return render_template("index.html", headline=puzzle)
