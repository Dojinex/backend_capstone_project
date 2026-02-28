from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from .models import ClassRoom, Subject, Schedule
from .serializers import ClassRoomSerializer, SubjectSerializer, ScheduleSerializer
from accounts.permissions import IsAdminOrTeacher


# -------------------------
# Pagination
# -------------------------
class StandardPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 50


# -------------------------
# ClassRoom ViewSet
# -------------------------
class ClassRoomViewSet(viewsets.ModelViewSet):
    serializer_class = ClassRoomSerializer
    permission_classes = [IsAdminOrTeacher]
    pagination_class = StandardPagination

    def get_queryset(self):
        user = self.request.user

        if user.role == "ADMIN":
            return ClassRoom.objects.all()

        elif user.role == "TEACHER" and hasattr(user, "teacher"):
            # Fixed field name from 'teacher' -> 'class_teacher'
            return ClassRoom.objects.filter(class_teacher=user.teacher)

        else:  # STUDENT
            return ClassRoom.objects.filter(students__user=user)


# -------------------------
# Subject ViewSet
# -------------------------
class SubjectViewSet(viewsets.ModelViewSet):
    serializer_class = SubjectSerializer
    permission_classes = [IsAdminOrTeacher]
    pagination_class = StandardPagination

    def get_queryset(self):
        user = self.request.user

        if user.role == "ADMIN":
            return Subject.objects.all()

        elif user.role == "TEACHER" and hasattr(user, "teacher"):
            # Replace with correct FK field to teacher in Subject model
            return Subject.objects.filter(teacher=user.teacher)

        else:  # STUDENT
            return Subject.objects.filter(class_room__students__user=user)


# -------------------------
# Schedule ViewSet
# -------------------------
class ScheduleViewSet(viewsets.ModelViewSet):
    serializer_class = ScheduleSerializer
    permission_classes = [IsAdminOrTeacher]
    pagination_class = StandardPagination

    def get_queryset(self):
        user = self.request.user

        if user.role == "ADMIN":
            return Schedule.objects.all()

        elif user.role == "TEACHER" and hasattr(user, "teacher"):
            # Replace with correct FK field to teacher in Schedule model
            return Schedule.objects.filter(teacher=user.teacher)

        else:  # STUDENT
            return Schedule.objects.filter(class_room__students__user=user)