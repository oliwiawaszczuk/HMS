# Generated by Django 4.2.7 on 2023-12-10 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meets', '0003_alter_meet_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meet',
            name='room',
            field=models.CharField(max_length=25),
        ),
    ]
