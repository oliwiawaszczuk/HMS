from django.db import models

class Test(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField(default=0)
    # czy refundowane?, sala do wykonania?, terminy?


# class Examination(models.Model):
#     test = models.ForeignKey(Test, )