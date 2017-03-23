from lib/bottle import route, run

@route('/installation')
def hello():
    return "Hello World!"
    request.query.id

from bottle import route, request, response, template
@route('/installation')
def installation():
    sport = request.query.sport
    
    #return template('Forum ID: {{id}} (page {{page}})', id=forum_id, page=page)
    return sport


run(host='localhost', port=9999, debug=True)
