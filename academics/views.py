from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import ClassRoom, Subject, Schedule
from .serializers import (
    ClassRoomSerializer,
    SubjectSerializer,
    ScheduleSerializer
)

from accounts.permissions import IsAdminOrTeacher


class ClassRoomViewSet(viewsets.ModelViewSet):
    queryset = ClassRoom.objects.all()
    serializer_class = ClassRoomSerializer
    permission_classes = [IsAdminOrTeacher]


class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [IsAdminOrTeacher]


class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    permission_classes = [IsAdminOrTeacher]