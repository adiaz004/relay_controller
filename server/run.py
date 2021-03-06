from logging import debug
from flask.helpers import send_from_directory
import markdown
import shelve
from flask import Flask, g, render_template
from flask_restful import Api, Resource
from flask_cors import CORS
from relay_api.relay_set_mode import RelaySetMode
from relay_api.relay import Relay
from relay_api.relays import Relays
from relay_api.relay_status import RelayStatus
import sys

app = Flask(__name__)
CORS(app)
api = Api(app)

def get_db():
    """
    setup shelve db
    """
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
    # with open('./README.md', 'r') as markdown_file:
    #     content = markdown_file.read()
    #     return markdown.markdown(content)
    return render_template("index.html", flask_token="Hello")

api.add_resource(Relays, '/relays',
    resource_class_kwargs={'db': get_db})
api.add_resource(Relay, '/relay/<id>',
    resource_class_kwargs={'db': get_db})
api.add_resource(RelayStatus, '/relay/<id>/status',
    resource_class_kwargs={'db': get_db})
api.add_resource(RelaySetMode, '/relay/<id>/mode/<mode>', 
    resource_class_kwargs={'db': get_db})

app.run(host="0.0.0.0", port=80, debug=True)
