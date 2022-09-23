import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "attendance_tracker.settings")
django.setup()

from students.models import Department,Student,Classroom
from users.models import CustomUser

import random
import string

class_count = 0
class_id = 6

for x in range(400,402):

    if class_count<60:
        classroom =Classroom.objects.get(id=class_id)
        class_count = class_count +1
    else:
        class_id = class_id+1
        class_count = 0

    user = CustomUser.objects.get(id=x+2)
    roll_number= user.username

    student = Student(
    user_id = x,
    roll_number=roll_number,
    classroom=classroom)

    student.save()
    print(roll_number,x,user,classroom,student.user_id)
