import csv
import http.client
from urllib.parse import urlencode
import json
from urllib import request


API_KEY ="ntWIq3E6VJyaoTFIRPSCa39KQJZwDgGo"


try:
    location = input('Entrez une adresse : ')

    urlParams = {'location': location, 'key': API_KEY, 'inFormat':'kvp', 'outFormat':'json'}
    url = "http://www.mapquestapi.com/geocoding/v1/address?" + urlencode(urlParams)

    print(url)

    proxy_host = 'proxyetu.iut-nantes.univ-nantes.prive:3128'
    req = request.Request(url)
    req.set_proxy(proxy_host, 'http')

    response = request.urlopen(req)

    data = response.read().decode('utf8')

    jsonData = json.loads(data)
    # FIXME le print n'est pas très secure...
    print(jsonData['results'][0]['locations'][0]['latLng']['lat'])
    print("test")
    print(jsonData['results'][0]['locations'][0]['latLng']['lng'])
except Exception as err:
    print("Unexpected error: {0}".format(err))