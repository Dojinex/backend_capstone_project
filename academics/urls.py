from rest_framework.routers import DefaultRouter
from .views import (
    ClassRoomViewSet,
    SubjectViewSet,
    ScheduleViewSet
)

router = DefaultRouter()
router.register(r'classes', ClassRoomViewSet, basename='class')
router.register(r'subjects', SubjectViewSet, basename='subject')
router.register(r'schedules', ScheduleViewSet, basename='schedule')

urlpatterns = router.urls