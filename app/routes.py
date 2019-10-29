from app import app, db
from flask import request, jsonify
from app.models import Data
import uuid
import subprocess
import sys
import os


@app.route("/")
@app.route("/submit", methods=['POST'])
def submit():
    if request.method == "POST":
        new = Data()
        new.id = uuid.uuid1().hex
        new.url = request.form.get('url')
        if new.url:
            subprocess.Popen([sys.executable, 'app\hashing.py']
                       + [new.id, new.url],
                       stdout=subprocess.PIPE,
                       stderr=subprocess.STDOUT,
                       env=os.environ.copy())
        else:
            return(jsonify('Error 400 url not given'))
        new.md5_hash = ""
        new.email = request.form.get('email')
        new.state = "working"
        db.session.add(new)
        db.session.commit()
    return(new.id)

@app.route("/check", methods=['GET'])
def check():
    if request.method == "GET":
        id1 = request.form.get('id')
    data = Data.query.get(id1)
    if not data:
        return('Error 404 id not found')
    if data.state == 'finished':
        return('state: ' + data.state + ', \nhash: ' + data.md5_hash + '\nurl: ' + data.url)
    else:
        return('state: ' + data.state)