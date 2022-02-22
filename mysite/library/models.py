from django.db import models

# Create your models here.
class Authors(models.Model):
    biography = models.CharField(max_length=5000)
    name = models.CharField(max_length=15)
    surname = models.CharField(max_length=30)
    patronymic = models.CharField(max_length=20)

class Genres(models.Model):
    title = models.CharField(max_length=30)

class Books(models.Model):
    authors = models.ForeignKey(Authors, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    year = models.IntegerField(max_length=4)
    publication_house = models.CharField(max_length=15)
