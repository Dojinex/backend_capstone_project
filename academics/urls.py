from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import ClassRoomViewSet, SubjectViewSet, ScheduleViewSet

# Initialize DRF router
router = DefaultRouter()
router.register(r'classes', ClassRoomViewSet, basename='class')
router.register(r'subjects', SubjectViewSet, basename='subject')
router.register(r'schedules', ScheduleViewSet, basename='schedule')

# Include router URLs in urlpatterns
urlpatterns = [
    path('', include(router.urls)),
]