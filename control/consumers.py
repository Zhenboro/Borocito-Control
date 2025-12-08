import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

# Create your consumers here.

class InstanceController(WebsocketConsumer):
    
    def connect(self):
        self.uuid = self.scope["url_route"]["kwargs"]["uuid"]
        self.instance_uuid = f"instance_{self.uuid}"
        
        async_to_sync(self.channel_layer.group_add)(
            self.instance_uuid, self.channel_name
        )
        
        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.instance_uuid, self.channel_name
        )
    
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        
        async_to_sync(self.channel_layer.group_send)(
            self.instance_uuid, {"type": "instance.message", "message": text_data_json}
        )
    
    def instance_message(self, event):
        text_data_json = event['message']
        if 'command' in text_data_json:
            command = text_data_json['command']
            self.send(text_data=json.dumps({"command": command}))
        
        if 'response' in text_data_json:
            response = text_data_json['response']
            self.send(text_data=json.dumps({"response": response}))
