from flask import Flask
from flask_restful import Api, Resource

app  =Flask(__name__)
api = Api(app)

# Resource class to handle requests
class Test(Resource):
    def get(self):
        return {'data': 'Stand by for a test'}
# get resource needs always needs to be serializable

api.add_resource(Test, "/test")
# Root of the resource and where it is accessible

 #REMOVE True in production!
if __name__ == "__main__":
    app.run(debug=True)   