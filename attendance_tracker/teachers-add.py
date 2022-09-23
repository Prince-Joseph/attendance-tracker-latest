import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "attendance_tracker.settings")
django.setup()

from teachers.models import Teacher
from students.models import Department
from users.models import CustomUser

import random
import string

for x in range(8,100):
    z = random.randint(1,6)
    user = CustomUser.objects.get(id=x)
    dept = Department.objects.get(id = z)
    teacher = Teacher(
     user= user,
     department= dept)
    print(x,user,dept,z)
    teacher.save()