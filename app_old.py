from flask import Flask
from flask_restful import Api, Resource

app  =Flask(__name__)
api = Api(app)

# Resource class to handle requests
# Resource object needs to be ALWAYS serializable (JSON format)
messages = {'Cisco': {'Interview': 1, 'Role': 'Python Developer'},
            'Webex': {'Interview': 1, 'Role': 'Flask Developer'},
            'Zensar': {'Interview': 1, 'Role': 'RESTful Developer'}}

class Test(Resource):
    def get(self, message):
        return messages[message]

    # def post(self):
    #      return {'message': message}

# Root of the resource, where it is accessible and content

api.add_resource(Test, "/test/<string:message>")

#REMOVE True in production!

if __name__ == "__main__":
    app.run(debug=True)   