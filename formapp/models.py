from django.db import models
# Create your models here.
class Name(models.Model):
    First_name=models.CharField(max_length=10)
    Last_name=models.CharField(max_length=10)
