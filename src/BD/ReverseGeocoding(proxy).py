import csv
import http.client
from urllib.parse import urlencode
import json
from urllib import request
import sqlite3
import sys
import os

"""
Bout de code permettant de, pour chaque adresse d'installation, de trouver ses coordonnées géographiques et de les enregistrer dans la BD
"""


API_KEY = os.environ['mapquestapiKEY']


try:
    con = sqlite3.connect('test.db')
    cur = con.cursor()
    curUpdate = con.cursor()

    cur.execute('SELECT numero, adresse, ville from installation where latitude=0 and longitude=0')
    for row in cur:
        
        numero=str(row[0])
        location=row[1]+" "+row[2]+" France"

        urlParams = {'location': location, 'key': API_KEY, 'inFormat':'kvp', 'outFormat':'json'}
        url = "http://www.mapquestapi.com/geocoding/v1/address?" + urlencode(urlParams)

        proxy_host = 'proxyetu.iut-nantes.univ-nantes.prive:3128'
        req = request.Request(url)
        req.set_proxy(proxy_host, 'http')

        response = request.urlopen(req)

        data = response.read().decode('utf8')

        jsonData = json.loads(data)

        latitude = str(jsonData['results'][0]['locations'][0]['latLng']['lat'])
        longitude = str(jsonData['results'][0]['locations'][0]['latLng']['lng'])
        

        curUpdate.execute("UPDATE installation SET latitude = "+latitude+" WHERE numero="+numero)
        curUpdate.execute("UPDATE installation SET longitude = "+longitude+" WHERE numero="+numero)


except Exception as err:
    print("Unexpected error: {0}".format(err))
finally:
    con.commit()
    cur.close()
    curUpdate.close()
    con.close()
