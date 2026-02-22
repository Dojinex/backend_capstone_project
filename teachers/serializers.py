from rest_framework import serializers
from .models import Teacher
from accounts.models import User


class TeacherSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.filter(role="TEACHER")
    )

    class Meta:
        model = Teacher
        fields = "__all__"