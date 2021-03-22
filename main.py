import requests
from flask import Flask, request
from flask_restplus import Resource, Api

app = Flask(__name__)
api = Api(app)


@api.route('/api/v1/ping', methods=['POST'])
class Ping(Resource):
    def post(self):
        input = request.json
        url = input['url']
        with requests.get(url, verify=False) as resp:
            return resp.json()


@api.route('/health', methods=['GET'])
class LivenessCheck(Resource):
    def get(self):
        return {'message': 'healthy'}


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='8080')
