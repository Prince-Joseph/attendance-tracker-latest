# Generated by Django 4.1.1 on 2022-09-06 16:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teachers', '0001_initial'),
        ('students', '0003_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='teachers.subject')),
                ('teacher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='teachers.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Timetable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week_day', models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday')], default='Monday', max_length=10)),
                ('classroom', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='students.classroom')),
                ('period_1', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='period1_lecture', to='timetable.lecture')),
                ('period_2', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='period2_lecture', to='timetable.lecture')),
                ('period_3', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='period3_lecture', to='timetable.lecture')),
                ('period_4', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='period4_lecture', to='timetable.lecture')),
                ('period_5', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='period5_lecture', to='timetable.lecture')),
                ('period_6', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='period6_lecture', to='timetable.lecture')),
                ('period_7', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='period7_lecture', to='timetable.lecture')),
            ],
        ),
    ]
