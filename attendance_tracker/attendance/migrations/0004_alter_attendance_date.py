# Generated by Django 4.1.1 on 2022-09-13 05:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0003_attendance_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, null=True),
        ),
    ]
