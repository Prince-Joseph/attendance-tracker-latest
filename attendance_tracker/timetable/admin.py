from django.contrib import admin
from timetable.models import Timetable, Lecture
# Register your models here.
admin.site.register(Timetable)
admin.site.register(Lecture)