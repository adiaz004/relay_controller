from flask_restful import Resource, reqparse

class Relays(Resource):
    def __init__(self, db):
        self.get_db = db

    def get(self):
        shelf = self.get_db()
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
        shelf = self.get_db()
        shelf[args['id']] = args
        return {
            'message': 'Relay added',
            'data': args
        }, 201