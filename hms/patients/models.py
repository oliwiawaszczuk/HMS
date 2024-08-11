import datetime
from django.db import models
from workers.models import Worker


GENDER_CHOICES = [
    ('male', 'Mężczyzna'),
    ('female', 'Kobieta'),
]

TERRAIN_CHOICES = [
    ('zachodnio-pomorskie', 'Zachodnio-Pomorskie'),
    ('pomorskie', 'Pomorskie'),
    ('warminsko-pomorskie', 'Warmińsko-Pomorskie'),
    ('podlaskie', 'Podlaskie'),
    ('lubelskie', 'Lubelskie'),
    ('mazowieckie', 'Mazowieckie'),
    ('kujawsko-pomorskie', 'Kujawsko-Pomorskie'),
    ('wielkopolskie', 'Wielkopolskie'),
    ('lubuskie', 'Lubuskie'),
    ('dolnoslaskie', 'Dolnośląskie'),
    ('slaskie', 'Śląskie'),
    ('opolskie', 'Opolskie'),
    ('lodzkie', 'Łódzkie'),
    ('swietokrzyskie', 'Świętokrzyskie'),
    ('malopolskie', 'Małopolskie'),
    ('podkarpackie', 'Podkarpackie'),
]

class Patient(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    pesel = models.CharField(max_length=11)
    phone_numer = models.CharField(max_length=9)
    gender = models.CharField(choices=GENDER_CHOICES, default='male', max_length=20)
    terrain = models.CharField(choices=TERRAIN_CHOICES, default='lubelskie', max_length=40)
    city = models.CharField(max_length=50, default="")
    birthday = models.DateField()
    join_date = models.DateField(default=datetime.date.today)
    description = models.TextField(default="", null=True)

    def get_age(self):
        today_date = datetime.date.today()
        if self.birthday.month > today_date.month or self.birthday.month == today_date.month and self.birthday.day > today_date.day:
            return today_date.year - self.birthday.year - 1
        else:
            return today_date.year - self.birthday.year
    age = property(get_age)


class Appointment(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Worker, on_delete=models.CASCADE, null=True)
    cost = models.PositiveIntegerField(default=0)
    date = models.DateField()
    description = models.TextField(default="", null=True)

class Prescription(models.Model):
    pass

class Test(models.Model):
    pass

# historia leczenia
# ile wizyt, kiedy, po co
# recepty, daty
# jakie badania, kiedy, ile kosztowaly, czy refundowane