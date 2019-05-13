from django.db import models

# Create your models here.


class Actor (models.Model):
    name = models.CharField(max_length=255)
    image_URL = models.URLField(max_length=255)


class Genre(models.Model):
    type = models.CharField(max_length=255)


class Movie(models.Model):
    title = models.CharField(max_length=255)
    code=models.IntegerField()
    score = models.FloatField()
    audience = models.IntegerField()
    summary = models.TextField()
    poster_URL = models.URLField(max_length=255)
    actors = models.ManyToManyField(Actor, related_name="movie")
    genres = models.ManyToManyField(Genre, related_name="movie")
    sales = models.IntegerField()
    open_date=models.DateField()


# class Youtube(models.Model):
#     link = models.CharField(max_length=255)
#     movie = models.ForeignKey(
#         Movie, on_delete=models.CASCADE, related_name="youtube")


class Rating(models.Model):
    comment = models.TextField()
    score = models.FloatField()
    actor = models.ForeignKey(
        Actor, on_delete=models.CASCADE, related_name="rating")
