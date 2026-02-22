from rest_framework import serializers
from .models import ClassRoom, Subject, Schedule


class ClassRoomSerializer(serializers.ModelSerializer):
    class_teacher = serializers.StringRelatedField()

    class Meta:
        model = ClassRoom
        fields = "__all__"


class SubjectSerializer(serializers.ModelSerializer):
    teacher = serializers.StringRelatedField()

    class Meta:
        model = Subject
        fields = "__all__"


class ScheduleSerializer(serializers.ModelSerializer):
    class_room = serializers.StringRelatedField()
    subject = serializers.StringRelatedField()
    teacher = serializers.StringRelatedField()

    class Meta:
        model = Schedule
        fields = "__all__"