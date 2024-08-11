from django.db import models

# informacje o lekach
class Drug(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    expiration_date = models.CharField(max_length=7)
