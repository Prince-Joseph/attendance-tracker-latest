import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "attendance_tracker.settings")
django.setup()

from timetable.models import Timetable,Lecture
from students.models import Classroom
import random



def periodz(): return random.randint(1,12)


classes_id = 2
for week_day in range(0,6):
    for period_int in range(1,8):
        time_table = Timetable()
        
        time_table.classroom = Classroom.objects.get(id=classes_id)
        
        if week_day == 0:
            time_table.week_day = Timetable.WeekDay.MONDAY
        if week_day == 1:
            time_table.week_day = Timetable.WeekDay.TUESDAY
        if week_day == 2:
            time_table.week_day = Timetable.WeekDay.WEDNESDAY
        if week_day == 3:
            time_table.week_day = Timetable.WeekDay.THURSDAY
        if week_day == 4:
            time_table.week_day = Timetable.WeekDay.FRIDAY
        if week_day == 5:
            time_table.week_day = Timetable.WeekDay.SATURDAY

        time_table.lecture = Lecture.objects.get(id=periodz())
        time_table.period_no = period_int
        
        print(period_int,time_table.classroom,time_table.lecture,time_table.week_day)
        time_table.save()


        
# for x in range(1,13):

#     for y in range(0,6):
#         time_table = Timetable()
#         time_table.classroom = Classroom.objects.get(id=x)
#         if y == 0:
#             time_table.week_day = Timetable.WeekDay.MONDAY
#         if y == 1:
#             time_table.week_day = Timetable.WeekDay.TUESDAY
#         if y == 2:
#             time_table.week_day = Timetable.WeekDay.WEDNESDAY
#         if y == 3:
#             time_table.week_day = Timetable.WeekDay.THURSDAY
#         if y == 4:
#             time_table.week_day = Timetable.WeekDay.FRIDAY
#         if y == 5:
#             time_table.week_day = Timetable.WeekDay.SATURDAY


#         time_table.period_1= Lecture.objects.get(id=periodz())
#         time_table.period_2= Lecture.objects.get(id=periodz())
#         time_table.period_3= Lecture.objects.get(id=periodz())
#         time_table.period_4= Lecture.objects.get(id=periodz())
#         time_table.period_5= Lecture.objects.get(id=periodz())
#         time_table.period_6= Lecture.objects.get(id=periodz())
#         time_table.period_7= Lecture.objects.get(id=periodz())

#         print(time_table.week_day)
#         time_table.save()
#     print(x,time_table.classroom)


