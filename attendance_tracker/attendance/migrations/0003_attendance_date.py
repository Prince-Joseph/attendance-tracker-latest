# Generated by Django 4.1.1 on 2022-09-13 05:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0002_alter_attendance_period'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 9, 13, 5, 56, 23, 137508, tzinfo=datetime.timezone.utc), null=True),
        ),
    ]
