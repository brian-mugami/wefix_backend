from django.shortcuts import render
from rest_framework import viewsets, status
# Create your views here.
from rest_framework.response import Response
from .models import LocationModel, WorkTypeModel, UserModel
from .producer import publish
from .serializers import LocationSerializer, WorktypeSerializer, UserSerializer


class UserView(viewsets.ViewSet):
    def list(self, request):
        users = UserModel.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def create(self, request):
        user = UserSerializer(data=request.data)
        user.is_valid(raise_exception=True)
        user.save()
        return Response(data=user.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        user = UserModel.objects.get(id=pk)
        if not user:
            return Response({"message": "user not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        user = UserModel.objects.get(id=pk)
        serializer = LocationSerializer(user)
        if not user:
            return Response({"message": "location not found"}, status=status.HTTP_404_NOT_FOUND)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, pk=None):
        user = UserModel.objects.get(id=pk)
        if not user:
            return Response({"message": "location not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(instance=user, data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)

class LocationAPIVIEW(viewsets.ViewSet):
    def create(self, request):
        location = LocationSerializer(data=request.data)
        location.is_valid(raise_exception=True)
        location.save()
        publish("location_created", location.data)
        return Response(data=location.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        location = LocationModel.objects.get(id=pk)
        if not location:
            return Response({"message": "location not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = LocationSerializer(location)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def list(self, request):
        locations = LocationModel.objects.all()
        serializer = LocationSerializer(locations, many=True)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        location = LocationModel.objects.get(id=pk)
        serializer = LocationSerializer(location)
        if not location:
            return Response({"message": "location not found"}, status=status.HTTP_404_NOT_FOUND)
        location.delete()
        publish("location deleted", serializer.data)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, pk=None):
        location = LocationModel.objects.get(id=pk)
        if not location:
            return Response({"message": "location not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = LocationSerializer(instance=location, data=request.data)
        serializer.is_valid()
        serializer.save()
        publish("location updated", serializer.data)
        return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)

class WorktypeAPIVIEW(viewsets.ViewSet):
    def create(self, request):
        serializer = WorktypeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish("worktype created", serializer.data)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        worktype = WorkTypeModel.objects.get(id=pk)
        if not worktype:
            return Response({"message": "worktype not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = LocationSerializer(worktype)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def list(self, request):
        worktypes = WorkTypeModel.objects.all()
        serializer = LocationSerializer(worktypes, many=True)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        worktype = WorkTypeModel.objects.get(id=pk)
        serializer = LocationSerializer(worktype)
        if not worktype:
            return Response({"message": "worktype not found"}, status=status.HTTP_404_NOT_FOUND)
        worktype.delete()
        publish("worktype deleted", serializer.data)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, pk=None):
        worktype = WorkTypeModel.objects.get(id=pk)
        if not worktype:
            return Response({"message": "worktype not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = WorktypeSerializer(instance=worktype, data=request.data)
        serializer.is_valid()
        serializer.save()
        publish("worktype updated", serializer.data)
        return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)