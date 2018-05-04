import json
from django.conf import settings
from channels.generic.websocket import JsonWebsocketConsumer

class ChatConsumer(JsonWebsocketConsumer):

    def connect(self):
        if 'user_id' in self.scope['session']:
            print('CONNECTION FROM SOCKET INITIATED')
            self.accept()
        else:
            print('CONNECTION CLOSED USER IS NOT LOGGED IN')
            self.close()

    def receive_json(self, content):
        pass

    def disconnect(self, close_code):
        pass
