from datetime import datetime
from ninja import Schema, ModelSchema
from tracks.models import Track


class TrackSchema(ModelSchema):
    class Config:
        model = Track
        model_fields = ["title", "artist", "last_play", "duration"]


class NotFoundSchema(Schema):
    message: str
