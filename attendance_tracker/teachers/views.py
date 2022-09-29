from django.shortcuts import render

def teachers_dashboard(request):

    """
    displays teachers dashboard 
    """
    context={}
    # context['timetable']= Timetable.get_daywise_timetable(Timetable,1)
    return render(request,"teachers_dashboard.html",context)

# def URLView(request,student_id):
    # student_id=user
    # return redirect('http://localhost:3000/')

# def daywise_timetable_t(request,weekday):
#     """
#     displays teachers day wise timetable 
#     """ 
    
#     context={}
#     weekday=Timetable.objects.get(week_day=weekday)
#     context['daywise-attendance']=Timetable.get_daywise_timetable(Timetable,weekday)
#     return render(request,"teachers_dashboard.html",context)