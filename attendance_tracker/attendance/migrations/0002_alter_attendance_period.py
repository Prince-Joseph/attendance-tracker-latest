# Generated by Django 4.1.1 on 2022-09-06 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='period',
            field=models.IntegerField(blank=True, default=1),
        ),
    ]