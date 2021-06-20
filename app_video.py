from flask import Flask
from flask_restful import Api, Resource, reqparse

#REMOVE DEBUG

app  =Flask(__name__)
api = Api(app)

video_put_args = reqparse.RequestParser()
video_put_args.add_argument('room', type=str, help='Name of the room is required', required=True)
video_put_args.add_argument('participant', type=str, help='Name of the participant is required', required=True)
video_put_args.add_argument('spectators', type=int, help='Number of spectators is required', required=True)

videos = {}

class Video_Stream(Resource):
    def get(self, video_id):
        return videos[video_id]
    
    def put(self, video_id):
        args = video_put_args.parse_args()
        videos[video_id] = args
        return videos[video_id], 201


api.add_resource(Video_Stream, "/Video_Streaming/<int:video_id>")

if __name__ == "__main__":
    app.run(debug=True)   