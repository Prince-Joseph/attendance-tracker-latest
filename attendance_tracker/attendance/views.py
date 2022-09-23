import time
from rest_framework import viewsets
from django.http import HttpResponse
from rest_framework import views
from django.shortcuts import render
from teachers.models import Teacher, Subject
from attendance.models import Attendance,timezone
from students.models import Student, Classroom


from .serializers import ClasswiseStudentSerializer


def attendance_input(request, classroom_id, period_id, subject_id):
    """
     Displays React Page
    """

    context = {}
    return render(request, "attendance_input.html", context)


class ClasswiseStudent(viewsets.ModelViewSet):
    """
    Serializer for classroom data
    """
    queryset = Student.objects.filter(classroom=1)
    serializer_class = ClasswiseStudentSerializer


class ClasswiseStudentAPI(viewsets.generics.ListAPIView):
    """
    API VIEW of Classroom Data
    """
    serializer_class = ClasswiseStudentSerializer

    def get_queryset(self):
        # print(self.kwargs['class_room'])
        #  /clarromapi/1/1/2/
        # sdjkskds/<id:classroom_id>/        # classroom = self.kwargs['classroom_id'] # id of classroom
        # classroom = self.kwargs['period_id'] # id of classroom
        class_room = self.kwargs['classroom_id']
        # period = self.kwargs['period_id']
        # subject = self.kwargs['subject_id']

        students = Student.objects.filter(classroom=class_room)
        return students


class SaveAttendance(views.APIView):
    """
    saves fetched data into attendance model
    """
    # Post
    def post(self, request, format=None):
        start_time = time.time()
        object_data = request.data  # from react JSON

        print(object_data)
        
        if object_data:
            student_data = object_data['student_data']
        # print(object_data)
        classroom_id = Classroom.objects.get(id=object_data['classroom_id'])
        # teacher_id = Teacher.objects.get(id=request.user.id)
        period_no =  object_data["period"]
        teacher_id = Teacher.objects.get(id=1)
        subject_id = Subject.objects.get(id=object_data['subject_id'])

        """
        try:
            oldata =  Attendance.get(dat=,per,classroom,)
            old_data = Attendance.Objects.get(period =, classroom_id =, subject_id=, teacher_id=, date=)

            entry = Entry.objects.get(pk=123)
            if some_queryset.filter(pk=entry.pk).exists():
                    print("Entry contained in queryset")






        except Error:
            #data doesnt exist
            # create new records with accpeted
            
        else:
            #
            #old data so check and updateit
        """
        

        # If common headers match with previous record just update the
        # rows
        for i in range(0, student_data.length):

            attendance_record = Attendance()

            print(student_data[i]['rollNumber'])
            # 19k81A0340

            attendance_record.classroom = classroom_id
            attendance_record.period = period_no
            attendance_record.teacher = teacher_id
            attendance_record.subject = subject_id

            rollNumber = student_data[i]['rollNumber']

            student_id = Student.objects.get(roll_number=rollNumber)
            attendance_record.student = student_id  # id

            # print(student_data[i]['isPresent']) # true/false
            if student_data[i].get('isPresent') is not None:
                attendance_record.is_present = student_data[i]['isPresent']
            else:
                attendance_record.is_present = False

            attendance_record.save()

            end_time = time.time()
            # print("Record", i, end_time-start_time)

        end_time = time.time()
        # print("Total Time Taken", end_time-start_time," seconds", "from_classrom",object_data['classroom_id'])
        return HttpResponse('data_saved')

def attendance_summary (request,classroom_id,period_id):
    """
    returns attendance summary of a particular pediod(presentees,absentees)
    """
    context = {}
    date = timezone.now()
    print(date)
    # x = Student.objects.filter()

    # roll_Number=Student.rollNumber

    # x = students from specific class, specific period, specific date
    x = Attendance.objects.filter(classroom=classroom_id,period=period_id,date=date)

    context["attendance_summary"] = x

    # x = Attendance.objects.filter(classroom=classroom_id)
    # context["attendance_summary"] = x
    return render(request, "attendance_summary.html", context)




# Emulating Hundred  Record
"""
for y in range(1, 105):
    rollNumberaa = f"19K81A{str(y).rjust(4, '0')}"  # make it 3
    student_data.append(
        {"rollNumber": rollNumberaa, "isPresent": True})
# print(student_data)
"""