# Generated by Django 4.2.7 on 2023-12-11 05:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meets', '0006_alter_meet_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meet',
            name='date',
            field=models.DateField(default=datetime.date(2023, 12, 11)),
        ),
    ]
