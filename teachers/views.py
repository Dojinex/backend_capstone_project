from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend

from .models import Teacher
from .serializers import TeacherSerializer
from accounts.permissions import IsAdmin

# Custom pagination for teachers
class TeacherPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 50


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.select_related("user").all()
    serializer_class = TeacherSerializer
    permission_classes = [IsAuthenticated, IsAdmin]  # Only admin can manage teachers
    pagination_class = TeacherPagination

    # Filtering, Search, Ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # Fields to filter by (exact match)
    filterset_fields = ["department", "subject"]

    # Fields to search by
    search_fields = ["user__username", "user__email", "user__first_name", "user__last_name"]

    # Fields to order by
    ordering_fields = ["user__first_name", "user__last_name", "department"]
    ordering = ["user__first_name"]  # default ordering