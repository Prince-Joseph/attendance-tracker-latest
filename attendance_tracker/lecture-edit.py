import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "attendance_tracker.settings")
django.setup()

from timetable.models import Lecture
from teachers.models import Teacher,Subject

subject_count = 0
subject_id = 1
for x in range(4,100):
    lecture = Lecture.objects.get(id=x)
    lecture.subject = Subject.objects.get(id=x) 
    lecture.save()