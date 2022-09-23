from django.db import models
from users.models import CustomUser
from students.models import Department


class Teacher(models.Model):
    """
    Teachers Model connects to Custom User
    """
    user = models.OneToOneField(CustomUser,on_delete=models.PROTECT)
    department= models.ForeignKey(Department,on_delete=models.PROTECT)

    def __str__(self):
        return str(self.user.name)

class Subject(models.Model):

    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

    def __str__(self):
        return  str(self.code) 

