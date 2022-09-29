import datetime
from django.db import models
from students.models  import Student,Classroom
from teachers.models import Subject,Teacher
from django.utils import timezone

class Attendance(models.Model):
    """
    Stores List of All students attendance
    """
    date= models.DateField(default=timezone.now)
    classroom = models.ForeignKey(Classroom, on_delete=models.PROTECT)
    period = models.IntegerField(default=1, blank=True) # first / 2nd
    student = models.ForeignKey(Student, null=True, blank=True, on_delete=models.PROTECT)
    teacher = models.ForeignKey(Teacher,null=True, blank=True, on_delete=models.PROTECT)
    is_present = models.BooleanField(blank=True)
    subject = models.ForeignKey(Subject, null=True,blank=True,on_delete=models.PROTECT)

    def __str__(self):
        return self.student.roll_number + " " +  " "+ str(self.period)

    # Attendance.gettodayasattence(Attendace,student)
    def get_todays_attendance(self,student):
        todays_attendance = Attendance.objects.filter(student=student,date=timezone.now())
        return todays_attendance

    def get_specific_date_attendance(self,student,date):
        todays_attendance = Attendance.objects.filter(student=student,date=date)
        return todays_attendance

    def get_subjectwise_attendance(self,student,subject):
        subjectwise_attendance= Attendance.objects.filter(student=student,subject=subject)
        return subjectwise_attendance

    def get_semesterwise_attendance(self,student):
        semesterwise_attendence = Attendance.objects.filter(student=student)
        return semesterwise_attendence

    def get_date_attendance_score(self,student,date):
        date = datetime.date(2022,9,18)
        all_records_from_that_date = Attendance.objects.filter(student=student,date=date)
        score = 0
        for x in all_records_from_that_date:
            if x.is_present:
                score = score+1
        return score



