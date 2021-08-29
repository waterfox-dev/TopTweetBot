from flask import Flask, render_template
from source.api_reader import *


app = Flask(__name__)

@app.route('/')
def index() :
    today_picture = read_today()["imageLink"]
    return render_template("index.html", today_post = today_picture)