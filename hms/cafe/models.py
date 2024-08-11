from django.db import models

# ile w magazynie, ile sprzedano - raporty
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
