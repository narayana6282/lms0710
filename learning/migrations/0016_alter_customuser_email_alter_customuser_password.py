# Generated by Django 5.0.1 on 2024-01-08 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0015_delete_students'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(default='', max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='password',
            field=models.CharField(default='', max_length=255),
        ),
    ]
