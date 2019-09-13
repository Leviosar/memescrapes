#!/usr/bin/env python

from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps
from search import search, search_image, search_meme
from slugify import slugify

app = Flask(__name__)
api = Api(app)

class Meme(Resource):
    def get(self, search_needle):
        return search(slugify(search_needle))

class Image(Resource):
    def get(self, search_needle):
        return search_image(slugify(search_needle))

api.add_resource(Meme, '/meme', '/meme/<string:search_needle>')
api.add_resource(Image, '/image', '/image/<string:search_needle>')

if __name__ == '__main__':
    app.run(debug=True)