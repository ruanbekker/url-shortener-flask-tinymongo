from flask import Flask, request, jsonify, Response, redirect
from tinymongo import TinyMongoClient

domain = 'http://localhost:5000/u/'

c = TinyMongoClient('tinydb')
db_init = c.mydb
db = db_init.records

def check_duplicates(url_id):
    db_result = db.find_one({"url_id": url_id })
    if db_result == None:
        id_exists = 'no'
    else:
        id_exists = db_result

    return id_exists

def create_tiny(full_url):
    url_id = generate_id()
    check_id_existence = check_duplicates(url_id)
    if check_id_existence == 'no':
        tiny_url = domain + url_id
        doc = db.insert_one({'url_id': url_id, 'url_original': full_url, 'url_short': tiny_url}).inserted_id
        return 'Your TinyURL is: <a href="{}">{}</a>'.format(tiny_url, tiny_url)
    else:
        return 'URL Already Exists: {0}'.format(check_id_existence['url_short'])

def get_url_response(tiny_url):
    get_url = db.find_one({'url_short': tiny_url})['url_original']
    return 'Your Full URL is: {}'.format(get_url)

def get_url(tinyid):
    url = db.find_one({"url_id": tinyid})['url_original']
    return url

app = Flask(__name__)

@app.route('/')
def index():
    return 'OK'

@app.route('/create/<path:fullurl>')
def index(fullurl):
    response = create_tiny(fullurl)
    return response

@app.route('/check/<path:tinyurl>')
def get(tinyurl):
    response = get_url_response(tinyurl)
    return response

@app.route('/u/<tinyid>')
def redirect_it(tinyid):
    full_url = get_url(tinyid)
    return redirect(full_url)

if __name__ == '__main__':
    app.run()
