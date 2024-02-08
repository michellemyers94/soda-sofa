

import logging
logging.basicConfig(level=logging.DEBUG)

from google.cloud import datastore
from google.cloud import storage
import os
# Set the environment variable
# os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'C:\Users\Michelle\Downloads\sodasofa-fde66b03eb2a.json'

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
from werkzeug.utils import secure_filename

from dotenv import load_dotenv, find_dotenv
from flask import Flask
from flask import jsonify

from flask import session
from flask import url_for
from authlib.integrations.flask_client import OAuth
from six.moves.urllib.parse import urlencode
from datetime import datetime
import pytz
from flask_caching import Cache

app = Flask(__name__, template_folder='templates')

# app.secret_key = 'SECRET_KEY'

cache = Cache(app, config={'CACHE_TYPE': 'simple'})

client = datastore.Client()

# Initialize GCP Storage Client
storage_client = storage.Client()
bucket_name = 'image_posts'
bucket = storage_client.bucket(bucket_name)



# Initialize GCP Storage Client
storage_client = storage.Client()

# Print the service account email
# print(f"Storage client's service account email: {storage_client._credentials.service_account_email}")
print("hello world")
print(os.getenv('GOOGLE_APPLICATION_CREDENTIALS'))
print("hello world")
bucket_name = 'image_posts'
bucket = storage_client.bucket(bucket_name)


POSTS = "posts"
COMMENTS = "comments"

