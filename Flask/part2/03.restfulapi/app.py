from flask import Flask, request
from flask_restful import Api
from resources.item import Item

app = Flask(__name__)

api = Api(app)


api.add_resource(Item, '/item/<string:name>')

if __name__ == '__main__':
    app.run(debug=True)



    