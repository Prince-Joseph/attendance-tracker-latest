import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "attendance_tracker.settings")
django.setup()

from users.models import CustomUser

import random
import string

# Users
for x in range(108,400):
    user = CustomUser()
    rolls= "19K81A"+str(x).rjust(4, '0') # make it 3
    user.set_password(rolls)
    user.phone_number = random.randint(800,700000)
    user.email=f"{random.choice(string.ascii_uppercase)}{random.choice(string.ascii_uppercase)}{random.choice(string.ascii_uppercase)}{random.choice(string.ascii_uppercase)}{random.choice(string.ascii_uppercase)}{random.choice(string.ascii_uppercase)}{random.choice(string.ascii_uppercase)}{random.choice(string.ascii_uppercase)}{random.choice(string.ascii_uppercase)}{random.choice(string.ascii_uppercase)}{random.choice(string.ascii_uppercase)}{random.choice(string.ascii_uppercase)}{random.choice(string.ascii_uppercase)}"+"@gmail.com"
    user.name = f"{random.choice(string.ascii_uppercase)}{random.choice(string.ascii_lowercase)}{random.choice(string.ascii_lowercase)}"
    user.username= rolls
    print(user.phone_number,x)
    user.save()