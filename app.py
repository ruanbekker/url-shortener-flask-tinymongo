from flask import Flask, request, jsonify, Response, redirect
from tinymongo import TinyMongoClient

domain = 'http://localhost:5000/u/'

c = TinyMongoClient('tinydb')
db_init = c.mydb
db = db_init.records

app = Flask(__name__)

@app.route('/')
def index():
    return 'OK'

if __name__ == '__main__':
    app.run()
