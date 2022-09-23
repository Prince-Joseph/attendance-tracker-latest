import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "attendance_tracker.settings")
django.setup()

from timetable.models import Lecture
from teachers.models import Teacher,Subject

subject_count = 0
subject_id = 1
for x in range(1,100):
    lecture = Lecture()
    
    subject_count=+1
    if subject_count>3:
        subject_id=+1
    
    lecture.subject = Subject.objects.get(id=subject_id) 
    lecture.teacher = Teacher.objects.get(id=x)
    lecture.save()