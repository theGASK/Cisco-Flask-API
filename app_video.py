from flask import Flask
from flask_restful import Api, Resource, reqparse

#REMOVE DEBUG

app  =Flask(__name__)
api = Api(app)

video_put_args = reqparse.RequestParser()
videos = {}

class Video_Stream(Resource):
    def get(self, video_id):
        return videos[video_id]
    
    def put(self, video_id):

        return


api.add_resource(Video_Stream, "/Video_Streaming/<int:video_id>")

if __name__ == "__main__":
    app.run(debug=True)   