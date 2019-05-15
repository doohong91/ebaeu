from django.db import models
from django.conf import settings
from django.db.models import Avg
# Create your models here.


class Actor (models.Model):
    name = models.CharField(max_length=255)
    image = models.URLField(max_length=255)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_actors', blank=True)

    @property
    def get_point(self):
        avg_score = float(self.movies.aggregate(Avg('score'))['score__avg'])
        avg_aud = float(self.movies.aggregate(Avg('normalized_audience'))['normalized_audience__avg'])
        avg_sales = float(self.movies.aggregate(Avg('normalized_sales'))['normalized_sales__avg'])
        return round(sum([avg_score, avg_aud, avg_sales])/3, 4)


class Genre(models.Model):
    type = models.CharField(max_length=255)


class Movie(models.Model):
    code=models.IntegerField()
    title = models.CharField(max_length=255)
    score = models.FloatField()
    sales = models.IntegerField()
    normalized_sales = models.FloatField()
    audience = models.IntegerField()
    normalized_audience = models.FloatField()
    open_date=models.DateField()
    poster_URL = models.URLField(max_length=255)
    summary = models.TextField()
    actors = models.ManyToManyField(Actor, related_name="movies")
    genres = models.ManyToManyField(Genre, related_name="movies")
    viewed_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='viewed_movies', blank=True)


# class Youtube(models.Model):
#     link = models.CharField(max_length=255)
#     movie = models.ForeignKey(
#         Movie, on_delete=models.CASCADE, related_name="youtube")


class Rating(models.Model):
    comment = models.TextField()
    score = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    actor = models.ForeignKey(
        Actor, on_delete=models.CASCADE, related_name="ratings")
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="ratings")
    