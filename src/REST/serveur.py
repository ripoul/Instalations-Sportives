import sqlite3
from lib.bottle import route, run, template, request

@route('/installation')
def installation():
	ville = request.query.ville
	sport = request.query.sport

	db = sqlite3.connect('test.db')
	c = db.cursor()

	if(ville!="all" and sport!="all"):
		c.execute("SELECT e.nom, i.nom, i.adresse, i.code_postal, i.ville from installation i, equipement e, equipement_activite ea, activite a where i.numero=e.numero_installation and e.numero=ea.numero_equipement and ea.numero_activite=a.numero and a.numero=\""+sport+"\" and i.ville=\""+ville+"\";")
	if(ville=="all" and sport!="all"):
		c.execute("SELECT e.nom, i.nom, i.adresse, i.code_postal, i.ville from installation i, equipement e, equipement_activite ea, activite a where i.numero=e.numero_installation and e.numero=ea.numero_equipement and ea.numero_activite=a.numero and a.numero=\""+sport+"\";")
	if(ville!="all" and sport=="all"):
		c.execute("SELECT e.nom, i.nom, i.adresse, i.code_postal, i.ville from installation i, equipement e, equipement_activite ea, activite a where i.numero=e.numero_installation and e.numero=ea.numero_equipement and ea.numero_activite=a.numero and i.ville=\""+ville+"\";")
	if(ville=="all" and sport=="all"):
		c.execute("SELECT e.nom, i.nom, i.adresse, i.code_postal, i.ville from installation i, equipement e, equipement_activite ea, activite a where i.numero=e.numero_installation and e.numero=ea.numero_equipement and ea.numero_activite=a.numero;")
	

	output = template('src/IHM/resultat.tpl', rows=c)
	c.close()
	return output

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

run(host='localhost', port=9999, debug=True)