from django.db import models

# Create your models here.
class Book(models.Model):
    Title=models.CharField(max_length=30)
    Author=models.CharField(max_length=30)
    Isbn=models.CharField(max_length=30)
    Publisher=models.DateField()