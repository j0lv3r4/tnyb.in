import bottle
from tnybin import app
from config import PORT, HOST, DEBUG

bottle.run(app=app, host=HOST, port=PORT, debug=DEBUG,
           reloader=True)
