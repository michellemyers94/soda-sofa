import logging

logging.basicConfig(level=logging.DEBUG)

from google.cloud import datastore
from flask import Flask, request, jsonify, _request_ctx_stack, render_template, redirect
import requests
import logging
import urllib.parse
from urllib.parse import quote_plus

from functools import wraps
import json

from six.moves.urllib.request import urlopen
from flask_cors import cross_origin
from jose import jwt

import json
from os import environ as env
from werkzeug.exceptions import HTTPException

from dotenv import load_dotenv, find_dotenv
from flask import Flask
from flask import jsonify

from flask import session
from flask import url_for
from authlib.integrations.flask_client import OAuth
from six.moves.urllib.parse import urlencode

app = Flask(__name__, template_folder='templates')

# app.secret_key = 'SECRET_KEY'

client = datastore.Client()

POSTS = "posts"
COMMENTS = "comments"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.j2')

@app.route('/upload')
def upload():
    return render_template('upload.j2')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
