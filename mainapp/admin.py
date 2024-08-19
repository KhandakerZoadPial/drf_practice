from django.contrib import admin
from .models import Teacher

# Register your models here.
# admin.site.register(Teacher)

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'name', 'course_name', 'duration', 'seats'
    ]