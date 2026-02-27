from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend

from .models import ClassRoom, Subject, Schedule
from .serializers import ClassRoomSerializer, SubjectSerializer, ScheduleSerializer
from accounts.permissions import IsAdminOrTeacher

# Pagination classes
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

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['name']  # exact match filtering
    search_fields = ['name']     # search by name
    ordering_fields = ['name']   # ordering
    ordering = ['name']          # default ordering

    def get_queryset(self):
        user = self.request.user
        if user.role == "ADMIN":
            return ClassRoom.objects.all()
        elif user.role == "TEACHER":
            # Only classes assigned to this teacher
            return ClassRoom.objects.filter(teacher=user.teacher)
        else:  # STUDENT
            # Only student's class
            return ClassRoom.objects.filter(students__user=user)

# -------------------------
# Subject ViewSet
# -------------------------
class SubjectViewSet(viewsets.ModelViewSet):
    serializer_class = SubjectSerializer
    permission_classes = [IsAdminOrTeacher]
    pagination_class = StandardPagination

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['class_room', 'teacher']
    search_fields = ['name', 'teacher__user__first_name', 'teacher__user__last_name']
    ordering_fields = ['name', 'teacher__user__first_name']
    ordering = ['name']

    def get_queryset(self):
        user = self.request.user
        if user.role == "ADMIN":
            return Subject.objects.all()
        elif user.role == "TEACHER":
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

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['class_room', 'subject', 'teacher']
    search_fields = [
        'class_room__name',
        'subject__name',
        'teacher__user__first_name',
        'teacher__user__last_name'
    ]
    ordering_fields = ['class_room__name', 'subject__name', 'teacher__user__first_name']
    ordering = ['class_room__name']

    def get_queryset(self):
        user = self.request.user
        if user.role == "ADMIN":
            return Schedule.objects.all()
        elif user.role == "TEACHER":
            return Schedule.objects.filter(teacher=user.teacher)
        else:  # STUDENT
            return Schedule.objects.filter(class_room__students__user=user)