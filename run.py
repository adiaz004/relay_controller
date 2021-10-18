from logging import debug
import markdown
import shelve
from flask import Flask, g
from flask_restful import Api, Resource
from relay_registery.relay_set_mode import RelaySetMode
from relay_registery.relay import Relay
from relay_registery.relays import Relays
from relay_registery.relay_status import RelayStatus
import sys

app = Flask(__name__)
api = Api(app)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._databse = shelve.open("relays.db")
    return db

@app.teardown_appcontext
def teardown_db(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def index():
    """
    display documentation
    """
    with open('./README.md', 'r') as markdown_file:
        content = markdown_file.read()
        return markdown.markdown(content)

api.add_resource(Relays, '/relays',
    resource_class_kwargs={'db': get_db})
api.add_resource(Relay, '/relay/<id>',
    resource_class_kwargs={'db': get_db})
api.add_resource(RelayStatus, '/relay/<id>/status',
    resource_class_kwargs={'db': get_db})
api.add_resource(RelaySetMode, '/relay/<id>/mode/<mode>', 
    resource_class_kwargs={'db': get_db})

app.run(host="0.0.0.0", port=80, debug=True)