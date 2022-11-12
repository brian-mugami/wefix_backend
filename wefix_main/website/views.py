from flask_smorest import Blueprint,abort
from flask.views import MethodView
from .schemas import LocationSchema
from .models import LocationModel

location = Blueprint("location", __name__, description="Location resource")

@location.route("/location")
class LocationResource(MethodView):
    @location.response(200, LocationSchema(many=True))
    def get(self):
        locations = LocationModel.query.all()
        return locations
