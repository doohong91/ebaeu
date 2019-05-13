from django.db import models

# Create your models here.


class Actor (models.Model):
    name = models.CharField(max_length=255)
    image = models.URLField(max_length=255)


class Genre(models.Model):
    type = models.CharField(max_length=255)


class Movie(models.Model):
    code=models.IntegerField()
    title = models.CharField(max_length=255)
    sales = models.IntegerField()
    audience = models.IntegerField()
    open_date=models.DateField()
    actors = models.ManyToManyField(Actor, related_name="movies")
    genres = models.ManyToManyField(Genre, related_name="movies")
    score = models.FloatField()
    summary = models.TextField()
    poster_URL = models.URLField(max_length=255)


# class Youtube(models.Model):
#     link = models.CharField(max_length=255)
#     movie = models.ForeignKey(
#         Movie, on_delete=models.CASCADE, related_name="youtube")


class Rating(models.Model):
    comment = models.TextField()
    score = models.FloatField()
    actor = models.ForeignKey(
        Actor, on_delete=models.CASCADE, related_name="ratings")
