# Generated by Django 4.2.7 on 2023-12-08 06:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0003_remove_meet_date_end_remove_meet_date_start_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Meet',
        ),
    ]
