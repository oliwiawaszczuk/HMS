from django.db import models
from django.utils import timezone
from workers.models import Worker
import datetime


class Meet(models.Model):
    id = models.AutoField(primary_key=True)
    workers = models.ManyToManyField(Worker, related_name='meets')
    title = models.CharField(max_length=50)
    date = models.DateField(default=datetime.date.today())
    start = models.TimeField(default=timezone.now)
    end = models.TimeField(default=timezone.now)
    room = models.CharField(max_length=25)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
