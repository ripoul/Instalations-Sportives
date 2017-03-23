from lib.bottle import route, request, response, template, run

@route('/installation')
def installation():
    ville = request.query.ville
    
    #return template('Forum ID: {{id}} (page {{page}})', id=forum_id, page=page)
    return ville

@route('/')
def installation():
        #return template('Forum ID: {{id}} (page {{page}})', id=forum_id, page=page)
    return "welcome"

run(host='localhost', port=9999, debug=True)
