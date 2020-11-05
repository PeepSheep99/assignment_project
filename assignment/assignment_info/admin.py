from django.contrib import admin

# Register your models here.
from .models import Course,Submissions,CourseSubmissions
admin.site.register(CourseSubmissions)
admin.site.register(Submissions)
admin.site.register(Course)
