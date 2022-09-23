from django.db import models
from users.models import CustomUser

class Department(models.Model):
    # id = 1 (hidden)
    code = models.CharField(max_length=4)
    name = models.CharField(max_length=60)

    def __str__(self):
        return str(self.name)

class Classroom(models.Model):
    department = models.ForeignKey(Department,null=True,blank=True,on_delete=models.PROTECT)
    year = models.IntegerField()
    section = models.CharField(max_length=30)


    # list of all students
    def __str__(self):
        classroom_id = self.department.code + str(self.year) + str(self.section)
        return classroom_id


class Student(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.PROTECT)

    roll_number = models.CharField(max_length=30)
    # rollNumber
    classroom = models.ForeignKey(Classroom, null=True,blank=True,on_delete=models.PROTECT)

    def __str__(self):
        return str(self.id) +" "+self.roll_number + " " + self.user.name

    class Meta:
        ordering = ['roll_number']





