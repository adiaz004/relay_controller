import markdown
import shelve
import os
from flask import Flask, g
from flask_restful import Api, Resource, reqparse

# from relay_registery.relays import Relays

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
    with open(os.path.dirname(app.root_path) + '/README.md', 'r') as markdown_file:
        content = markdown_file.read()
        return markdown.markdown(content)

class Relays(Resource):

    def get(self):
        shelf = get_db()
        keys = list(shelf.keys())
        relays = []
        for key in keys:
            relays.append(shelf[key])
        return {
            'message': 'Sucess',
            'data': relays
        }, 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', required=True)
        parser.add_argument('name', required=True)
        parser.add_argument('gpio', required=True)
        
        args = parser.parse_args()
        shelf = get_db()
        shelf[args['id']] = args
        return {
            'message': 'Relay added',
            'data': args
        }, 201

class Relay(Resource):

    def get(self, id):
        shelf = get_db()
        if not (id in shelf):
            return {'message': "relay not found", 'data': {}}, 404

        return {
            'message': 'Relay found',
            'data': shelf[id]
        }, 200

    def delete(self, id):
        shelf = get_db()
        if not (id in shelf):
            return {'message': "relay not found", 'data': {}}, 404
        del shelf[id]
        return '', 204

api.add_resource(Relays, '/relays')
api.add_resource(Relay, '/relay/<id>')