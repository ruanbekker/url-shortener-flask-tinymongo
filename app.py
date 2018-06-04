from flask import Flask, request, jsonify, Response, redirect
from tinymongo import TinyMongoClient

domain = 'http://localhost:5000/u/'

c = TinyMongoClient('tinydb')
db_init = c.mydb
db = db_init.records

def create_tiny(full_url):
    url_id = generate_id()
    check_id_existence = check_duplicates(url_id)
    if check_id_existence == 'no':
        tiny_url = domain + url_id
        doc = db.insert_one({'url_id': url_id, 'url_original': full_url, 'url_short': tiny_url}).inserted_id
        return 'Your TinyURL is: <a href="{}">{}</a>'.format(tiny_url, tiny_url)
    else:
        return 'URL Already Exists: {0}'.format(check_id_existence['url_short'])

app = Flask(__name__)

@app.route('/')
def index():
    return 'OK'

@app.route('/create/<path:fullurl>')
def index(fullurl):
    response = create_tiny(fullurl)
    return response

if __name__ == '__main__':
    app.run()
