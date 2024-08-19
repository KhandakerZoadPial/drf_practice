from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import io

from .models import Teacher
from .serializers import TeachersSerializer

# Create your views here.
def home(request):
    teacher_set = Teacher.objects.all()

    serialized_data = TeachersSerializer(teacher_set, many=True)

    json_data = JSONRenderer().render(serialized_data.data)

    return HttpResponse(json_data, content_type='application/json')


@csrf_exempt
def create_teacher(request):
    if request.method == 'POST':
        json_data = request.body
        # json to stream convrsion
        stream = io.BytesIO(json_data)
        # stream to python dict
        python_dict = JSONParser().parse(stream)

        serializer = TeachersSerializer(data=python_dict)

        if serializer.is_valid:
            serializer.save()
            res = {
                "message": "Successfully Inserted Data to Teacher."
            }

            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        else:
            json_data = JSONRenderer().render(serializer.errors)
            return HttpResponse(json_data, content_type='application/json')