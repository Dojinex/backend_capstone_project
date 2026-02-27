from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# -----------------------------
# URL Routing for the Project
# -----------------------------
urlpatterns = [
    # Django Admin
    path('admin/', admin.site.urls),

    # API Endpoints
    path('api/accounts/', include('accounts.urls')),
    path('api/teachers/', include('teachers.urls')),
    path('api/students/', include('students.urls')),
    path('api/academics/', include('academics.urls')),

    # JWT Authentication
    path('api/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # DRF Browsable API login for testing in browser
    path('api-auth/', include('rest_framework.urls')),
]