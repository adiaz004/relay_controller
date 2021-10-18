from flask_restful import Resource

class RelayStatus(Resource):
    def __init__(self, db):
        self.get_db = db
        
    def get(self, id=None):
        shelf = self.get_db()
        if not (id in shelf):
            return {'message': f"relay {id} not found", 'data': {}}, 404
        status = 1
        return {
            'message': f'relay {id} status',
            'data': status
        }, 200