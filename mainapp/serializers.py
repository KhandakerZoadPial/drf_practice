from rest_framework import serializers
from .models import Teacher


# class TeachersSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=20)
#     course_name = serializers.CharField(max_length=25)
#     duration = serializers.IntegerField(default=0)
#     seats = serializers.IntegerField(default=20)

#     def create(self, validated_data):
#         return Teacher.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.course_name = validated_data.get('course_name', instance.course_name)
#         instance.duration = validated_data.get('duration', instance.duration)
#         instance.seats = validated_data.get('seats', instance.seats)

#         instance.save()

#         return instance



class TeachersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['name', 'course_name', 'duration', 'seats']