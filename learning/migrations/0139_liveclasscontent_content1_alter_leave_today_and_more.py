# Generated by Django 5.0.1 on 2024-02-22 12:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0138_remove_staff_prob_p1_staff_imp_image2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='liveclasscontent',
            name='content1',
            field=models.CharField(default='', max_length=400),
        ),
        migrations.AlterField(
            model_name='leave',
            name='today',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 22, 12, 10, 15, 339187)),
        ),
        migrations.AlterField(
            model_name='teacher_shifts',
            name='half_daytime',
            field=models.TimeField(verbose_name=datetime.datetime(2024, 2, 22, 12, 10, 15, 318206)),
        ),
        migrations.AlterField(
            model_name='teacher_shifts',
            name='in_time',
            field=models.TimeField(verbose_name=datetime.datetime(2024, 2, 22, 12, 10, 15, 318206)),
        ),
        migrations.AlterField(
            model_name='teacher_shifts',
            name='late_mark_time',
            field=models.TimeField(verbose_name=datetime.datetime(2024, 2, 22, 12, 10, 15, 318206)),
        ),
        migrations.AlterField(
            model_name='teacher_shifts',
            name='out_time',
            field=models.TimeField(verbose_name=datetime.datetime(2024, 2, 22, 12, 10, 15, 318206)),
        ),
        migrations.AlterField(
            model_name='teachers',
            name='dob',
            field=models.DateField(default=datetime.datetime(2024, 2, 22, 12, 10, 15, 317235)),
        ),
    ]
