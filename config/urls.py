from django.contrib import admin
from django.urls import path, include
from academics.views import ClassRoomViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("classes", ClassRoomViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include(router.urls)),
]