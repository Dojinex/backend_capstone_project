from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend

from .models import Student
from .serializers import StudentSerializer
from accounts.permissions import ReadOnlyOrAdmin


class StudentPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 50


class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    permission_classes = [ReadOnlyOrAdmin]
    pagination_class = StudentPagination

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    filterset_fields = ["class_room"]
    search_fields = ["reg_number", "user__username", "user__email"]
    ordering_fields = ["reg_number"]
    ordering = ["reg_number"]

    def get_queryset(self):
        user = self.request.user

        if not user.is_authenticated:
            return Student.objects.none()

        role = getattr(user, "role", None)

        if user.is_staff or user.is_superuser or role == "ADMIN":
            return Student.objects.select_related(
                "user", "class_room"
            ).all()

        if role == "TEACHER" and hasattr(user, "teacher"):
            return Student.objects.select_related(
                "user", "class_room"
            ).filter(class_room__teacher=user.teacher)

        if role == "STUDENT":
            return Student.objects.select_related(
                "user", "class_room"
            ).filter(user=user)

        return Student.objects.none()