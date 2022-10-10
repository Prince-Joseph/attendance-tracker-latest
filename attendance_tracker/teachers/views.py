from django.shortcuts import render

def teachers_dashboard(request):

    """
    displays teachers dashboard 
    """
    context={}
    # context['timetable']= Timetable.get_daywise_timetable(Timetable,1)
    return render(request,"teachers_dashboard.html",context)

