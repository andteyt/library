from django.db import models

# Create your models here.
class Authors(models.Model):
    biography = models.TextField()
    name = models.CharField(max_length=15)
    surname = models.CharField(max_length=30)
    patronymic = models.CharField(max_length=20)
    img = models.ImageField(upload_to='img/author',
                      height_field=100, width_field=100)
class Genres(models.Model):
    title = models.CharField(max_length=30)

class Books(models.Model):
    authors = models.ForeignKey(Authors, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    year = models.IntegerField(max_length=4)
    publication_house = models.CharField(max_length=15)
class Books_Genres(models.Model):
    b_g_books = models.ForeignKey(Books, on_delete=models.CASCADE)
    b_g_genres = models.ForeignKey(Genres, on_delete=models.CASCADE)
