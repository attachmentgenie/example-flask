from flask import Flask
from flask.ext.cors import CORS
from flask.ext.restplus import Api, Resource

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
api = Api(app, version='1.0', title='Sample API',
    description='A sample API', default_label='Example Flask'
)

@api.route('/v1/hello/<name>', endpoint='nodes')
@api.doc(params={'name': 'Name'})
class MyResource(Resource):
    @api.doc(responses={200: 'OK'})
    def get(self, name):
        return {}

    @api.doc(responses={200: 'OK', 403: 'Not Authorized'})
    def post(self, name):
        api.abort(403)

if __name__ == '__main__':
    app.run(debug=True)