from django.contrib import admin
from .models import Student,Classroom,Department
# Register your models here.
admin.site.register(Student)
admin.site.register(Classroom)
admin.site.register(Department)