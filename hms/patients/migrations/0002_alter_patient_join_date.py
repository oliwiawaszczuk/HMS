# Generated by Django 4.2.7 on 2023-11-29 03:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='join_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
