from flask import Flask
from flask_restful import Api, Resource, abort, reqparse
from flask_sqlalchemy import SQLAlchemy

#REMOVE DEBUG

app  =Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)


class ConferenceModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    room = db.Column(db.String(100), nullable=False)
    spectators = db.Column(db.Integer, nullable=True)
    participants = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'Session(room ={room}, spectators={spectators}, participants={participants})'

# Remove once created
# db.create_all()

video_put_args = reqparse.RequestParser()
video_put_args.add_argument('room', type=str, help='Name of the room is required', required=True)
video_put_args.add_argument('participants', type=str, help='Name of the participant is required', required=True)
video_put_args.add_argument('spectators', type=int, help='Number of spectators is required', required=True)



# def video_exists(video_id):
#     if video_id in videos:
#         abort(409, message='Video already exists')

# def video_404(video_id):
#     if video_id not in videos:
#         abort(404, message='Video is not found')


class Video_Stream(Resource):
    def get(self, video_id):
        video_404(video_id)
        return videos[video_id]

    
    def put(self, video_id):
        video_exists(video_id)
        args = video_put_args.parse_args()
        videos[video_id] = args
        return videos[video_id], 201


    def delete(self, video_id):
        video_404(video_id)
        del videos[video_id]
        return 'Video deleted', 204




api.add_resource(Video_Stream, "/Video_Streaming/<int:video_id>")

if __name__ == "__main__":
    app.run(debug=True)   