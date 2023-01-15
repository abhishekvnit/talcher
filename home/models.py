from django.db import models


class tabledb(models.Model):
    sno= models.IntegerField()
    l2id= models.CharField(max_length=10)
    task= models.CharField(max_length=100)
    start= models.CharField(max_length=10)
    finish= models.CharField(max_length=10)

# Create your models here.
def __str__(self):
    return self.l2id+" "+ self.task