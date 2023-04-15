import flask
from flask_restful import Resource, Api
from scripts.main import main

app = flask.Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
 def get(self):main()


api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)