# Generated by Django 4.1.4 on 2023-02-22 09:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_feedback_created_alter_mynotes_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='Mobile',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='created',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 2, 22, 15, 2, 35, 685249)),
        ),
        migrations.AlterField(
            model_name='mynotes',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 2, 22, 15, 2, 35, 685249)),
        ),
        migrations.AlterField(
            model_name='usersignup',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 2, 22, 15, 2, 35, 685249)),
        ),
    ]
