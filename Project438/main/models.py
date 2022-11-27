from django.db import models

# Create your models here.
class Telephone(models.Model):
    name = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    tel_num = models.CharField(max_length=100)
    mob_num = models.CharField(max_length=100)