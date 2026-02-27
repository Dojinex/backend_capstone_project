from rest_framework import viewsets, filters, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend

from .models import User
from .serializers import UserSerializer
from accounts.permissions import IsAdmin

# -----------------------------
# Pagination for Users
# -----------------------------
class UserPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 50

# -----------------------------
# User CRUD ViewSet (Admin only)
# -----------------------------
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsAdmin]
    pagination_class = UserPagination

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # Fields to filter by exact match
    filterset_fields = ["role", "is_active"]

    # Fields to search
    search_fields = ["username", "email", "first_name", "last_name"]

    # Ordering
    ordering_fields = ["username", "email", "first_name", "last_name"]
    ordering = ["username"]

    def get_queryset(self):
        user = self.request.user
        # Only admin can access users
        if user.role == "ADMIN":
            return User.objects.all()
        return User.objects.none()  # safety: no one else can access users

# -----------------------------
# Public Registration Endpoint
# -----------------------------
class RegisterView(APIView):
    permission_classes = []  # public endpoint

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            # Hash password properly
            user.set_password(request.data["password"])
            user.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)