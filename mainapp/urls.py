from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('create_teacher', create_teacher, name='create_teacher')
]
