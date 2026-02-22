from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    class_assigned = serializers.StringRelatedField()

    class Meta:
        model = Student
        fields = "__all__"