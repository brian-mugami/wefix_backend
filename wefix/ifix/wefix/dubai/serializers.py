from rest_framework import serializers
from .models import UserModel, LocationModel, WorkTypeModel

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = "__all__"

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationModel
        fields = "__all__"

class WorktypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkTypeModel
        fields = "__all__"