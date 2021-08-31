from flask import Flask, render_template, request, jsonify
from source.api_reader import *


app = Flask(__name__)

@app.route('/')
def index() :
    today_picture = read_today()["imageLink"]
    return render_template("index.html", today_post = today_picture)

#API
@app.route('/api/by_id')
def api_by_id() :
    id = request.args.get('id', None)
    return jsonify(get_by_id(id))