#-*- coding: utf-8 -*-

from flask import Flask
from flask_restful import Resource, Api, abort, reqparse
from plugins import weather, exchange

import random

app = Flask(__name__)
api = Api(app)

headers = {'Accept': 'application/vnd.tosslab.jandi-v2+json',
           'Content-Type': 'application/json; charset=utf-8'}

parser = reqparse.RequestParser()
parser.add_argument('token')
parser.add_argument('teamName')
parser.add_argument('roomName')
parser.add_argument('writerName')
parser.add_argument('text')
parser.add_argument('keyword')
parser.add_argument('createdAt')

class Jandi(Resource):
    def post(self):
        args = parser.parse_args()
        text = args['text']

        try:
            command = text.split(' ')[2]
            if command == '날씨':
                res = weather.run(text.split(' ')[1])
            elif command == '환율':
                res = exchange.run(text.split(' ')[1])
        except:
            pass

        if '좋지' in text or '좋아' in text or '좋니' in text:
            data = random.choice(["네 좋아요!", "글쎄요 잘 모르겠어요", "당연하죠!", "사랑합니다.", "걍 일이나하죠?", "..."])
            res = "{body: %s}" % (data)
        return res, 200, headers

api.add_resource(Jandi, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

