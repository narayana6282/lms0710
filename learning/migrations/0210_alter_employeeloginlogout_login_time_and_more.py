# Generated by Django 4.1.3 on 2024-04-29 16:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0209_alter_employeeloginlogout_login_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeeloginlogout',
            name='login_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 29, 16, 43, 24, 367425)),
        ),
        migrations.AlterField(
            model_name='leave',
            name='today',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 29, 16, 43, 24, 426265)),
        ),
        migrations.AlterField(
            model_name='shift_names',
            name='end_time',
            field=models.TimeField(default=datetime.datetime(2024, 4, 29, 16, 43, 24, 362437)),
        ),
        migrations.AlterField(
            model_name='shift_names',
            name='start_time',
            field=models.TimeField(default=datetime.datetime(2024, 4, 29, 16, 43, 24, 362437)),
        ),
        migrations.AlterField(
            model_name='teacher_shifts',
            name='half_daytime',
            field=models.TimeField(verbose_name=datetime.datetime(2024, 4, 29, 16, 43, 24, 381385)),
        ),
        migrations.AlterField(
            model_name='teacher_shifts',
            name='in_time',
            field=models.TimeField(verbose_name=datetime.datetime(2024, 4, 29, 16, 43, 24, 381385)),
        ),
        migrations.AlterField(
            model_name='teacher_shifts',
            name='late_mark_time',
            field=models.TimeField(verbose_name=datetime.datetime(2024, 4, 29, 16, 43, 24, 381385)),
        ),
        migrations.AlterField(
            model_name='teacher_shifts',
            name='out_time',
            field=models.TimeField(verbose_name=datetime.datetime(2024, 4, 29, 16, 43, 24, 381385)),
        ),
        migrations.AlterField(
            model_name='teachers',
            name='dob',
            field=models.DateField(default=datetime.datetime(2024, 4, 29, 16, 43, 24, 379392)),
        ),
    ]
