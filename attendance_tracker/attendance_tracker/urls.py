from django.contrib import admin
from django.urls import path, include

from students.views import student_dashboard, specific_day_attendance, subjectwise_attendance, semesterwise_attendance
from teachers.views import teachers_dashboard
from attendance.views import ClasswiseStudentAPI, attendance_input, SaveAttendance,attendance_summary
from timetable.views import classroom_timetable,teachers_timetable

urlpatterns = [

    path('admin/', admin.site.urls),

    # acccounts contains login,logout etc..
    # ex: accounts/login and accounts/logout
    path('accounts/', include("django.contrib.auth.urls")),

    # path('',home) does a check and redirects 
    # user to respective page

    # Student
    # Student-dashboard
    path('dashboard/s/<int:student_id>/', student_dashboard),
    path('attendance/s/<int:student_id>/d/<int:year>/<int:month>/<int:date>/' ,specific_day_attendance, name='specific_date_attendance'),
    path('attendance/s/<int:student_id>/subject/<int:subject_id>/', subjectwise_attendance, name='subjectwise_attendance'),
    path('attendance/s/<int:student_id>/semester/',semesterwise_attendance, name='semester_attendance'),

    # Teachers
    path('dashboard/t/',teachers_dashboard),

    # Attendance
    # attendance-input [react page]
    path('attendance/<int:classroom_id>/<int:period_id>/<int:subject_id>/', attendance_input),
    # attendance classwise data serialiser [get] []
    path('classroom/<int:classroom_id>/', ClasswiseStudentAPI.as_view()),
    # attendance data input [post] []
    path('attendance/save/', SaveAttendance.as_view()),
    # attendace-summary
    path('attendance/summary/<int:classroom_id>/<int:period_id>/',attendance_summary),

    # Timetable
    # classroom student timetable
    path('timetable/c/<int:classroom_id>/', classroom_timetable,name="classroom_timetable"),
    # teacher wise timetable
    path('timetable/t/<int:teacher_id>/', teachers_timetable),


]
