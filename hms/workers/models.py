from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import time, timedelta
import datetime

professions = (
    ("ochroniarz", 'Ochroniarz'),
    ("sprzatacz", 'Sprzątacz'),
    ("barista", 'Barista'),
    ("farmaceuta", 'Farmaceuta'),
    ("recepcjonista", 'Recepcjonista'),
    ("pielegniarz", 'Pielęgniarz'),
    ("lekarz specjalista", 'Lekarz Specjalista'),
    ("ordynator", 'Ordynator'),
    ('dyrektor', 'Dyrektor'),
    ("lekarz naczelny", 'Lekarz naczelny')
)


class Worker(AbstractUser):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=10, unique=True, default="default_username")
    password = models.CharField(max_length=255)
    orginal_password = models.CharField(max_length=50, default="")
    name = models.CharField(max_length=35)
    surname = models.CharField(max_length=35)
    email = models.EmailField(max_length=50)
    phone_number = models.CharField(max_length=9, null=True)
    profession = models.CharField(choices=professions, default="ochroniarz", max_length=40)
    profession_description = models.TextField(default="", null=True)
    birthday = models.DateField(default=datetime.date.today())
    family_city = models.CharField(max_length=255, null=True)

    def get_full_name(self):
        return f"{self.profession} - {self.name} {self.surname}"

    def __str__(self):
        return self.get_full_name()

    def get_age(self):
        today_date = datetime.date.today()
        if self.birthday.month > today_date.month or self.birthday.month == today_date.month and self.birthday.day > today_date.day:
            return today_date.year - self.birthday.year - 1
        else:
            return today_date.year - self.birthday.year

    def get_number_format(self):
        number = self.phone_number
        if not number:
            return 0
        number_format = ' '.join(number[i:i + 3] for i in range(0, len(number), 3))
        return number_format


class WorkHours(models.Model):
    id = models.AutoField(primary_key=True)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    date = models.DateField()
    start = models.TimeField(default=time(0, 0))
    end = models.TimeField(default=time(0, 0))

    def get_count_of_hours(self):
        start_datetime = datetime.combine(datetime.min, self.start)
        end_datetime = datetime.combine(datetime.min, self.end)

        if end_datetime > start_datetime:
            duration = end_datetime - start_datetime
            return duration
        else:
            return timedelta(hours=0)

    get_count_of_hours = property(get_count_of_hours)


# class Appointment(models.Model):
#     title = # tytul, godzina, sala / tytul mozna dac z imieniem?

    # spotkanie, badanie, wizyta
