from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend

from .models import Student
from .serializers import StudentSerializer
from accounts.permissions import ReadOnlyOrAdmin

# Custom pagination for students
class StudentPagination(PageNumberPagination):
    page_size = 10  # default page size
    page_size_query_param = 'page_size'  # allow client to adjust page size
    max_page_size = 50  # max allowed

class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    permission_classes = [ReadOnlyOrAdmin]
    pagination_class = StudentPagination

    # Filtering, search, ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # Exact match filtering
    filterset_fields = ["class_room"]

    # Search by registration number or user info
    search_fields = ["reg_number", "user__username", "user__email", "user__first_name", "user__last_name"]

    # Ordering
    ordering_fields = ["reg_number", "user__first_name", "user__last_name", "class_room__name"]
    ordering = ["reg_number"]  # default ordering

    # Role-aware queryset
    def get_queryset(self):
        user = self.request.user
        if user.role == "ADMIN":
            return Student.objects.select_related("user", "class_room").all()
        elif user.role == "TEACHER":
            # Only students in the teacher's classes
            return Student.objects.select_related("user", "class_room").filter(
                class_room__teacher=user.teacher
            )
        else:  # STUDENT
            # Only the logged-in student
            return Student.objects.select_related("user", "class_room").filter(user=user)