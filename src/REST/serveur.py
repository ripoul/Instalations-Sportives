import sqlite3
from lib.bottle import route, run, template, request

@route('/installation')
def installation():
	ville = request.query.ville
	sport = request.query.sport

	db = sqlite3.connect('test.db')
	c = db.cursor()
	c.execute("SELECT i.nom, i.adresse, i.code_postal, i.ville from installation i, equipement e, equipement_activite ea, activite a where i.numero=e.numero_installation and e.numero=ea.numero_equipement and ea.numero_activite=a.numero and a.nom=\""+sport+"\" and i.ville=\""+ville+"\";")
	data = c.fetchall()
	c.close()
	output = template('src/IHM/resultat.tpl', rows=data)
	return output

@route('/')
def installation():
	#return template('Forum ID: {{id}} (page {{page}})', id=forum_id, page=page)
	output = template('src/IHM/Interface.tpl')
	return output

run(host='localhost', port=9999, debug=True)