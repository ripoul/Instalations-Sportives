import csv
import http.client
from urllib.parse import urlencode
import json


API_KEY ="AIzaSyDVhh9kdSNtwZGklnwbpQLOW3mB8qNnPno"



installations_data = csv.reader(open("data/csv/installationsMod.csv", "r"))



API_KEY = "YOUR_API_KEY"

try:
    location = input('Entrez une adresse : ')

    urlParams = {'location': location, 'key': API_KEY, 'inFormat':'kvp', 'outFormat':'json'}
    url = "/geocoding/v1/address?" + urlencode(urlParams)

    conn = http.client.HTTPConnection("www.mapquestapi.com")
    conn.request("GET", url)

    res = conn.getresponse()
    print(res.status, res.reason)

    data = res.read()
    jsonData = json.loads(data)
    # FIXME le print n'est pas très secure...
    print(jsonData['results'][0]['locations'][0]['latLng'])
except Exception as err:
    print("Unexpected error: {0}".format(err))
finally:
    conn.close()