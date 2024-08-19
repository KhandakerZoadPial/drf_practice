from rest_framework import serializers
from .models import Teacher


class TeachersSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20)
    course_name = serializers.CharField(max_length=25)
    duration = serializers.IntegerField(default=0)
    seats = serializers.IntegerField(default=20)

    def create(self, validated_data):
        return Teacher.objects.create(**validated_data)
