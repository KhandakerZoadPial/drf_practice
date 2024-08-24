from django.shortcuts import render
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser
# from django.http import HttpResponse
# from django.views.decorators.csrf import csrf_exempt
# import io

# import for api view
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Teacher
from .serializers import TeachersSerializer

# Create your views here.
@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def teacher(request, pk=None):
    if request.method == 'GET':
        if pk is None:
            teacher_set = Teacher.objects.all()
            serialized_teacher_set = TeachersSerializer(teacher_set, many=True)
            return Response(serialized_teacher_set.data)
        else:
            teacher = Teacher.objects.get(pk=pk)
            serialized_teacher = TeachersSerializer(teacher)
            return Response(serialized_teacher.data)
    if request.method == 'POST':
        data = request.data
        serialized_data = TeachersSerializer(data=data)

        if serialized_data.is_valid():
            serialized_data.save()
            return Response({"Message": "Successfully Inserted the data."})
        return Response(serialized_data.errors)
        
    if request.method == 'PUT' or request.method == 'PATCH':
        if request.method == 'PUT':
            serialized_data = TeachersSerializer(Teacher.objects.get(pk=pk), request.data)
        else:
            serialized_data = TeachersSerializer(Teacher.objects.get(pk=pk), request.data, partial=True)

        if serialized_data.is_valid():
            serialized_data.save()
            return Response({"Message": "Successfully updated your data."})
        return Response(serialized_data.errors)
    
    if request.method == 'DELETE':
        this_instance = Teacher.objects.get(pk=pk)
        this_instance.delete()
        return Response({"Successfully deleted data."})


































































# def home(request):
#     teacher_set = Teacher.objects.all()

#     serialized_data = TeachersSerializer(teacher_set, many=True)

#     json_data = JSONRenderer().render(serialized_data.data)

#     return HttpResponse(json_data, content_type='application/json')


# @csrf_exempt
# def teacher(request):
#     if request.method == 'POST':
#         json_data = request.body
#         # json to stream convrsion
#         stream = io.BytesIO(json_data)
#         # stream to python dict
#         python_dict = JSONParser().parse(stream)

#         serializer = TeachersSerializer(data=python_dict)

#         if serializer.is_valid():
#             serializer.save()
#             res = {
#                 "message": "Successfully Inserted Data to Teacher."
#             }

#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data, content_type='application/json')
#         else:
#             json_data = JSONRenderer().render(serializer.errors)
#             return HttpResponse(json_data, content_type='application/json')
    
#     if request.method == "PUT":
#         json_data = request.body
#         # json to stream
#         stream = io.BytesIO(json_data)
#         # stream to dict
#         python_dict = JSONParser().parse(stream)

#         this_instance = Teacher.objects.get(pk=python_dict["id"])


#         serializer = TeachersSerializer(this_instance, data=python_dict, partial=True)

#         if serializer.is_valid():
#             serializer.save()

#             res = {
#                 "message": "Successfully Updated Data to Teacher."
#             }

#             json_data = JSONRenderer().render(res)
#         else:
#             json_data = JSONRenderer().render(serializer.errors)
            
#         return HttpResponse(json_data, content_type='application/json')
    
#     if request.method == "DELETE":
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         python_dict = JSONParser().parse(stream)

#         id = python_dict["id"]

#         this_instance = Teacher.objects.get(pk=id)
#         this_instance.delete()

#         response = {
#             "message": "Successfully deleted the instance."
#         }

#         json_data = JSONRenderer().render(response)
#         return HttpResponse(json_data, content_type='application/json')