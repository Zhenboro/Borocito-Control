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
        if 'command' in text_data_json:
            command = text_data_json['command']
            self.send(text_data=json.dumps({
                'command': command
            }))
        if 'response' in text_data_json:
            response = text_data_json['response']
            self.send(text_data=json.dumps({
                'response': response
            }))
