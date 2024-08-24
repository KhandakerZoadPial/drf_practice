from django.urls import path
from .views import *

urlpatterns = [
    # path('', home),
    path('teacher', teacher, name='teacher'),
    path('teacher/<int:pk>', teacher, name='teacher')
]
