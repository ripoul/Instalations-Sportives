from lib.bottle import route, request, response, template, run
import csv
import http.client
from urllib.parse import urlencode
import json
from urllib import request
import sqlite3
import sys

@route('/installation')
def installation():
    ville = request.query.ville
    
    con = sqlite3.connect('test.db')
    cur = con.cursor()
    curUpdate = con.cursor()

    cur.execute('SELECT numero, adresse, ville from installation where latitude=0 and longitude=0')
    #return template('Forum ID: {{id}} (page {{page}})', id=forum_id, page=page)
    return ville

@route('/')
def installation():
        #return template('Forum ID: {{id}} (page {{page}})', id=forum_id, page=page)
    return "welcome"

run(host='localhost', port=9999, debug=True)
