# Generated by Django 5.0.1 on 2024-01-18 15:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0042_stdclass1_alter_teachers_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teachers',
            name='dob',
            field=models.DateField(default=datetime.datetime(2024, 1, 18, 15, 8, 9, 730206)),
        ),
    ]
