from typing import List, Optional
from ninja import NinjaAPI
from tracks.models import Track
from tracks.schema import TrackSchema, NotFoundSchema

api = NinjaAPI()


@api.get("/test")
def test(request):
    return {"message": "success!"}


@api.get("/tracks", response=List[TrackSchema])
def tracks(request, title: Optional[str] = None):
    if title:
        return Track.objects.filter(title__icontains=title)
    return Track.objects.all()


@api.get("/tracks/{track_id}", response={200: TrackSchema, 404: NotFoundSchema})
def track(request, track_id):
    try:
        track = Track.objects.get(pk=track_id)
        return 200, track
    except Track.DoesNotExist as e:
        return 404, {"message": "Could not find track"}


@api.post("/tracks", response={201: TrackSchema, 400: NotFoundSchema})
def create_track(request, track: TrackSchema):
    try:
        track = Track.objects.create(**track.dict())
        return 201, track
    except Exception as e:
        return 400, {"message": "Could not create track"}


@api.put("/tracks/{track_id}", response={200: TrackSchema, 400: NotFoundSchema})
def update_track(request, track_id: int, data: TrackSchema):
    try:
        track = Track.objects.get(pk=track_id)
        for attribute, value in data.dict().items():
            setattr(track, attribute, value)
        track.save()
        return 200, track
    except Track.DoesNotExist as e:
        return 404, {"message": "Could not find track"}
    except Exception as e:
        return 400, {"message": "Could not update track"}


@api.delete("/tracks/{track_id}", response={200: None, 400: NotFoundSchema})
def delete_track(request, track_id: int):
    try:
        track = Track.objects.get(pk=track_id)
        track.delete()
        return 200, None
    except Track.DoesNotExist as e:
        return 404, {"message": "Could not find track"}
    except Exception as e:
        return 400, {"message": "Could not delete track"}
