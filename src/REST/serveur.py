import sqlite3
from lib.bottle import route
from lib.bottle import run
from lib.bottle import template
from lib.bottle import request
from lib.bottle import static_file
from urllib.parse import urlencode
from urllib import request as req

@route('/recherche')
def recherche():
	ville = request.query.ville
	sport = request.query.sport

	db = sqlite3.connect('test.db')
	c = db.cursor()

	if(ville!="all" and sport!="all"):
		c.execute("SELECT e.nom, i.nom, i.adresse, i.code_postal, i.ville, i.latitude, i.longitude from installation i, equipement e, equipement_activite ea, activite a where i.numero=e.numero_installation and e.numero=ea.numero_equipement and ea.numero_activite=a.numero and a.numero=\""+sport+"\" and i.ville=\""+ville+"\";")
		output = template('src/IHM/resultat.tpl', rows=c)
	if(ville=="all" and sport!="all"):
		c.execute("SELECT e.nom, i.nom, i.adresse, i.code_postal, i.ville, i.latitude, i.longitude from installation i, equipement e, equipement_activite ea, activite a where i.numero=e.numero_installation and e.numero=ea.numero_equipement and ea.numero_activite=a.numero and a.numero=\""+sport+"\";")
		output = template('src/IHM/resultat.tpl', rows=c)
	if(ville!="all" and sport=="all"):
		c.execute("SELECT a.nom, e.nom, i.nom, i.adresse, i.code_postal, i.ville, i.latitude, i.longitude from installation i, equipement e, equipement_activite ea, activite a where i.numero=e.numero_installation and e.numero=ea.numero_equipement and ea.numero_activite=a.numero and i.ville=\""+ville+"\";")
		output = template('src/IHM/resultatSP.tpl', rows=c)
	if(ville=="all" and sport=="all"):
		c.execute("SELECT a.nom, e.nom, i.nom, i.adresse, i.code_postal, i.ville, i.latitude, i.longitude from installation i, equipement e, equipement_activite ea, activite a where i.numero=e.numero_installation and e.numero=ea.numero_equipement and ea.numero_activite=a.numero;")
		output = template('src/IHM/resultatSP.tpl', rows=c)

	c.close()
	return output

@route('/recherche/map')
def map():
	API_KEY ="TOow97ALT8euMLEjnd34wajjXB6AqiYL"

	#https://beta.mapquestapi.com/staticmap/v5/map?key=TOow97ALT8euMLEjnd34wajjXB6AqiYL&locations=46.45391,%20-0.693988||nantes,%20france|marker-lg-D51A1A-A20000&size=600,400@2x
	lat = request.query.lat
	longi = request.query.long
	ville = request.query.ref
	print(lat)
	print(longi)

	url="https://beta.mapquestapi.com/staticmap/v5/map?key=TOow97ALT8euMLEjnd34wajjXB6AqiYL&locations="+lat+",%20"+longi+"||"+ville+",%20france|marker-lg-D51A1A-A20000&size=600,400@2x"
	print(url)
	proxy_host = 'proxyetu.iut-nantes.univ-nantes.prive:3128'
	requ = req.Request(url)
	requ.set_proxy(proxy_host, 'http')
	response = req.urlopen(requ)


	output = open("src/IHM/img/img.jpg","wb")
	output.write(response.read())
	output.close()

	outpute = template('src/IHM/img.tpl')
	return outpute


@route('/')
def installation():
	db = sqlite3.connect('test.db')
	c = db.cursor()
	c.execute("SELECT numero, nom from activite order by nom asc;")
	data = c.fetchall()
	c.execute("SELECT DISTINCT ville from installation order by ville asc;")
	databis = c.fetchall()
	c.close()

	liste = [data, databis]
	output = template('src/IHM/Interface.tpl', rows=liste)
	return output


@route('/static/img/:filename')
def serve_static(filename):
	return static_file(filename, root='src/IHM/img/')


run(host='localhost', port=9999, debug=True)
