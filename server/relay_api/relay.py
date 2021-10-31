from flask_restful import Resource

class Relay(Resource):
    def __init__(self, db):
        self.get_db = db

    def get(self, id):
        shelf = self.get_db()
        if not (id in shelf):
                return {'message': f"relay {id} not found", 'data': {}}, 404

        return {
            'message': 'Relay found',
            'data': shelf[id]
        }, 200

    def delete(self, id):
        shelf = self.get_db()
        if not (id in shelf):
                return {'message': f"relay {id} not found", 'data': {}}, 404
        del shelf[id]
        return '', 204