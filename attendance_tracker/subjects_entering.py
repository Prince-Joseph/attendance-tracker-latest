# subjects_entering.py
# from teachers.models import Subject

    
import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "attendance_tracker.settings")
django.setup()

from teachers.models import Subject

from students.models import Department

import random
import string

for x in range(0,100):
    def rd(): return random.randint(1,6)
    x =rd()
    department = Department.objects.get(id=x).code
    def rd(): return random.randint(0,9)
    subject = Subject()
    if len(department)==3:
        subject.code = f"{department}{rd()}{random.choice(string.ascii_uppercase)}{random.choice(string.ascii_uppercase)}"
    else:
        subject.code = f"{department}{rd()}{rd()}{random.choice(string.ascii_uppercase)}{random.choice(string.ascii_uppercase)}"
    # print(subject.code)
    subject.save()