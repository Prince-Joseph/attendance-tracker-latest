from django.db import models
from traitlets import Integer
from students.models import Classroom
from teachers.models import Teacher, Subject
from django.utils.translation import gettext_lazy as _
import datetime

# kiranapproved


class Lecture(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT)
    teacher = models.ForeignKey(
        Teacher, null=True, blank=True, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.subject)+" "+str(self.teacher)


class Timetable(models.Model):

    class WeekDay(models.TextChoices):
        MONDAY = 'Monday', _('Monday')
        TUESDAY = 'Tuesday', _('Tuesday')
        WEDNESDAY = 'Wednesday', _('Wednesday')
        THURSDAY = 'Thursday', _('Thursday')
        FRIDAY = 'Friday', _('Friday')
        SATURDAY = 'Saturday', _('Saturday')

    classroom = models.ForeignKey(
        Classroom, null=True, blank=True, on_delete=models.PROTECT)
    week_day = models.CharField(
        max_length=10, default=WeekDay.MONDAY, choices=WeekDay.choices)

    period_no = models.IntegerField(null=True)
    lecture = models.ForeignKey( Lecture, on_delete = models.PROTECT, related_name='assigned_periods',null=True)
    # period_1 = models.ForeignKey(
    #     Lecture, on_delete=models.PROTECT, related_name="period1_lecture")
    # period_2 = models.ForeignKey(
    #     Lecture, on_delete=models.PROTECT, related_name="period2_lecture")
    # period_3 = models.ForeignKey(
    #     Lecture, on_delete=models.PROTECT, related_name="period3_lecture")
    # period_4 = models.ForeignKey(
    #     Lecture, on_delete=models.PROTECT, related_name="period4_lecture")
    # period_5 = models.ForeignKey(
    #     Lecture, on_delete=models.PROTECT, related_name="period5_lecture")
    # period_6 = models.ForeignKey(
    #     Lecture, on_delete=models.PROTECT, related_name="period6_lecture")
    # period_7 = models.ForeignKey(
    #     Lecture, on_delete=models.PROTECT, related_name="period7_lecture")

    

    def __str__(self):
        return str(self.period_no)+" "+ str(self.classroom) +" "+ self.week_day

    def get_unique_subject(self,classroom_id):
        all_relevant_timetables = Timetable.objects.filter(classroom=classroom_id)


    def get_daywise_timetable(self, classroom_id):

        """
        Students time table today
        """

        classroom = Classroom.objects.get(id=classroom_id)
        today = datetime.date.today()  # date
        # today = datetime.datetime.now() #datetime
        # someday = datetime.date(2002,6,2)
        current_weekday = datetime.date.weekday(today)
        print(classroom_id)
        # week in 0-6 --> 'Monday'
        day_ref = {
            0: 'Monday',
            1: 'Tuesday',
            2: 'Wednesday',
            3: 'Thursday',
            4: 'Friday',
            5: 'Saturday',
        }
        day = day_ref[current_weekday]
        print(Timetable.objects.filter(classroom=classroom,week_day=day))
        return Timetable.objects.filter(classroom=classroom,week_day=day)


