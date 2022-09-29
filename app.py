from flask import Flask, request
import hashlib
import hmac
import base64
import time
import requests
import json

class ChatbotMessageSender:

    ep_path = 'https://104rrd7b6s.apigw.ntruss.com/custom/v1/7399/67f52ed2b15be683f8b485047f01d9a1171d75bfda8b157531e3097d56d19643'

    secret_key = 'bVBaVlNxcUJVTURZSWxwUUlIWFhvTG5ScHNmWUh5eGY='

    def req_message_send(self,message):

        timestamp = self.get_timestamp()
        request_body = {
            'version': 'v2',
            'userId': 'U47b00b58c90f8e47428af8b7bddcda3d1111111',
            'timestamp': timestamp,
            'bubbles': [
                {
                    'type': 'text',
                    'data': {
                        'description': message
                    }
                }
            ],
            'event': 'send'
        }
        ## Request body
        encode_request_body = json.dumps(request_body).encode('UTF-8')
        ## make signature
        signature = self.make_signature(self.secret_key, encode_request_body)
        ## headers
        custom_headers = {
            'Content-Type': 'application/json;UTF-8',
            'X-NCP-CHATBOT_SIGNATURE': signature
        }

        print("## Timestamp : ", timestamp)
        print("## Signature : ", signature)
        print("## headers ", custom_headers)
        print("## Request Body : ", encode_request_body)
        
        response = requests.post(headers=custom_headers, url=self.ep_path, data=encode_request_body)
        return response

    @staticmethod
    def get_timestamp():
        timestamp = int(time.time() * 1000)
        return timestamp

    @staticmethod
    def make_signature(secret_key, request_body):
        secret_key_bytes = bytes(secret_key, 'UTF-8')
        signing_key = base64.b64encode(hmac.new(secret_key_bytes, request_body, digestmod=hashlib.sha256).digest())
        return signing_key

app = Flask(__name__)
@app.route('/chatbot', methods=['GET'])
def chatbot():
    message = request.args["message"]
    print(message)
    res = ChatbotMessageSender().req_message_send(message)
    jsonResponse = json.loads(res.text)
    print(jsonResponse)
    return jsonResponse
@app.route('/user/<user_name>/<int:user_id>')
def user(user_name, user_id):
    return f'Hello, {user_name}({user_id})!'
if __name__ == '__main__':
    app.run(debug=True)