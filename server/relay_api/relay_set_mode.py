from flask_restful import Resource
import RPi.GPIO as GPIO
import time

class RelaySetMode(Resource):
    def __init__(self, db):
        self.get_db = db

    def put(self, id=None, mode=0):
        shelf = self.get_db()
        if not (id in shelf):
            return {'message': f"relay {id} not found", 'data': {}}, 404
    
        relay = shelf[id]
        gpio = relay.gpio

        # do gpio toggle things
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(gpio, GPIO.OUT)
        
        GPIO.output(gpio, mode)

        return {
            'message': f'relay {id}',
            'data': mode
        }, 200