from flask import Flask, request 
import db

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World'

@app.route("/photos.json")
def index():
    return db.photos_all()
