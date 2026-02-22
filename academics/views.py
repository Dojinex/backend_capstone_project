from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import ClassRoom
from .serializers import ClassRoomSerializer


class ClassRoomViewSet(ModelViewSet):
    queryset = ClassRoom.objects.all()
    serializer_class = ClassRoomSerializer