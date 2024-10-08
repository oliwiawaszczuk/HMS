# Generated by Django 4.2.7 on 2023-11-28 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('pesel', models.CharField(max_length=11)),
                ('phone_numer', models.CharField(max_length=9)),
                ('gender', models.CharField(choices=[('women', 'Women'), ('men', 'Men')], default='women', max_length=5)),
                ('birthday', models.DateField()),
                ('join_date', models.DateField()),
            ],
        ),
    ]
