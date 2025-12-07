import json
from channels.generic.websocket import WebsocketConsumer

# Create your consumers here.

class SimpleEcho(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        self.close()   

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        expression = text_data_json['expression']
        self.send(text_data=json.dumps({
            'result': f"¡{expression}!"
        }))
