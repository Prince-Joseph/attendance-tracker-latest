from calendar import weekday
from datetime import date
from venv import create
from django.shortcuts import render
from teachers.models import Teacher
from timetable.models import Timetable,Lecture

def classroom_timetable(request,classroom_id):
    """
       displays students timetable
    """
    context={}
    timetable = Timetable.objects.filter(classroom=classroom_id)
    context["classroom_timetable"] = timetable
    return render(request,"timetable/classroom_timetable.html",context)

def teachers_timetable(request,teacher_id):
    """
    displays teachers timetable
    """

    context={}
    relevant_lectures_pk_queryset = Lecture.objects.filter(teacher=teacher_id)

    lectures_pk_list = []
    for query_item in relevant_lectures_pk_queryset:
        # [(1,),(4,),] --> [ 1, 4 ]
        lectures_pk_list.append(query_item)

    order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

    tables_period_1 = Timetable.objects.filter(period_1__in = lectures_pk_list)
    tables_period_2 = Timetable.objects.filter(period_2__in = lectures_pk_list)
    tables_period_3 = Timetable.objects.filter(period_3__in = lectures_pk_list)
    tables_period_4 = Timetable.objects.filter(period_4__in = lectures_pk_list)
    tables_period_5 = Timetable.objects.filter(period_5__in = lectures_pk_list)
    tables_period_6 = Timetable.objects.filter(period_6__in = lectures_pk_list)
    tables_period_7 = Timetable.objects.filter(period_7__in = lectures_pk_list)

    tables_period_1 = sorted(tables_period_1,key=lambda x: order.index(x.week_day))
    tables_period_2 = sorted(tables_period_2,key=lambda x: order.index(x.week_day))
    tables_period_3 = sorted(tables_period_3,key=lambda x: order.index(x.week_day))
    tables_period_4 = sorted(tables_period_4,key=lambda x: order.index(x.week_day))
    tables_period_5 = sorted(tables_period_5,key=lambda x: order.index(x.week_day))
    tables_period_6 = sorted(tables_period_6,key=lambda x: order.index(x.week_day))
    tables_period_7 = sorted(tables_period_7,key=lambda x: order.index(x.week_day))

    class aa():
        classroom = "period"
        week_day = "______"

    X= [aa]

    tables = tables_period_1  + X +tables_period_2 + X + tables_period_3+ X +tables_period_4+ X +tables_period_5+ X +tables_period_6+ X +tables_period_7
    context['tables'] = tables
    # tables = tables_period_1  + tables_period_2 + tables_period_3+ tables_period_4+ tables_period_5+ tables_period_6 + tables_period_7

    mondays = []
    tuesdays = []
    wednesdays = []
    thursdays = []
    fridays = []
    saturdays = []

    


    for x in tables:
        # print(x , x.week_day )
        if x.week_day == 'Monday':
            mondays.append(x)
        if x.week_day == 'Tuesday':
            tuesdays.append(x)
        if x.week_day == 'Wednesday':
            wednesdays.append(x)
        if x.week_day == 'Thursday':
            thursdays.append(x)
        if x.week_day == 'Friday':
            fridays.append(x)
        if x.week_day == 'Saturday':
            saturdays.append(x)


    # print("monday",dir(mondays[1]))

    context['monday'] = mondays
    context['tuesday'] = tuesdays
    context['wednesday'] = wednesdays
    context['thursday'] = thursdays
    context['friday'] = fridays
    context['saturday'] = saturdays

    # print(tables)

    return render(request, "timetable/teachers_timetable.html", context)
    # https://stackoverflow.com/questions/19745091/accessing-dictionary-by-key-in-django-template







def teachers_timetable(request,teacher_id):
    """
        Updated Teachers
    """
    context={}

    teacher = Teacher.objects.get(id=teacher_id)
    relevant_lectures_pk_queryset = Lecture.objects.filter(teacher=teacher_id)

    lectures_pk_list = []
    for query_item in relevant_lectures_pk_queryset:
        # [(1,),(4,),] --> [ 1, 4 ]
        lectures_pk_list.append(query_item)

    timetable = Timetable.objects.filter(lecture__in=lectures_pk_list)
   
    # print(timetable)
    # <QuerySet [<Timetable: 1 ME4A Monday>, <Timetable: 6 ME4A Monday>, 
    # <Timetable: 4 ME4A Tuesday>, <Timetable: 3 ME4B Tuesday>, <Timetable: 5 ME4B Tuesday>, 
    # <Timetable: 6 ME4B Wednesday>, <Timetable: 1 ME4B Friday>, <Timetable: 7 ME4B Saturday>]>

    context["teachers_timetable"] = timetable
    return render(request, "timetable/teachers_timetable.html", context)












"""
1. attendance models --> new creates
    if record already--> update
        period_id
        date
    else create

2. week wise data
    --> semester
    --> subjectwise

    model method which week

3. Teacher's timetable and template

4. Login system enforce on all views and test
"""