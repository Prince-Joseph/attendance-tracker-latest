import datetime
from django.shortcuts import render
from teachers.models import Subject
from students.models import Student
from attendance.models import Attendance
from timetable.models import Timetable

# Create your views here.
# def URLView(request):
#     return redirect('http://localhost:3000/')


def student_dashboard(request,student_id):
    """
    displays student dashhboard 
    """
    context={}
    student = Student.objects.get(id=student_id)
    date = datetime.date.today()
    context['student'] = student
    context['todays_attendance']= Attendance.get_specific_date_attendance(Attendance,student,date)
    context['timetable']= Timetable.get_daywise_timetable(Timetable,student.classroom.id)
    
    # # experiment
    # weekday=Timetable.objects.get(week_day=weekday)
    # print(x)
    # while(weekday== x):
    #     # student = Student.objects.get(id=student_id)  
    #      context['daywise-attendance']=Timetable.get_daywise_timetables(Timetable,weekday)
     
    return render(request,"student_dashboard.html",context)

def specific_day_attendance(request,student_id,year,month,date):
    """
    displays attendence of a specific day(yy/mm/dd)
    """
    context={}
    student = Student.objects.get(id=student_id)
    date = datetime.date(year,month,date)
    context['specific_date_attendance']= Attendance.get_specific_date_attendance(Attendance,student,date)
    return render(request,"specific_date_attendance.html",context)

def subjectwise_attendance(request,student_id,subject_id):
    """
    displays attendence summary per subject
    """
    context={}
    student= Student.objects.get(id=student_id)
    subject = Subject.objects.get(id=subject_id)
    context['subjectwise_attendance']=Attendance.get_subjectwise_attendance(Attendance,student,subject)
    return render(request,"subjectwise_attendance.html",context)

def semesterwise_attendance(request,student_id):
    """
    displays semester-wise attendance
    """
    context = {}
    student= Student.objects.get(id=student_id)
    context['semesterwise_attendance']=Attendance.get_semesterwise_attendance(Attendance,student)
    return render(request,"semwise_attendance.html",context)

# Not needed
def daywise_timetable(request,weekday):
    """
    displays that days' timetable
    """ 
    context={}
    weekday=Timetable.objects.get(week_day=weekday)
    context['daywise-attendance']=Timetable.get_daywise_timetable(Timetable,weekday)
    return render(request,"student_dashboard.html",context)