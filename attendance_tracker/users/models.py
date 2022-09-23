from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext as _

from users.managers import CustomUserManager

class CustomUser(AbstractUser):

    email = models.EmailField(_('email address'), unique=True)
    phone_number = models.IntegerField(unique=True,null=True)
    name = models.CharField(max_length=255,null=True)
    # user_id

    # USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('email',)

    objects = CustomUserManager()

    def __str__(self):
        return str(self.name)

