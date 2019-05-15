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
        avg_score = self.movies.aggregate(Avg('score'))['score__avg'] if self.movies.aggregate(Avg('score'))['score__avg'] else 0
        avg_aud = self.movies.aggregate(Avg('normalized_audience'))['normalized_audience__avg'] if self.movies.aggregate(Avg('normalized_audience'))['normalized_audience__avg'] else 0
        avg_sales = self.movies.aggregate(Avg('normalized_sales'))['normalized_sales__avg'] if self.movies.aggregate(Avg('normalized_sales'))['normalized_sales__avg'] else 0
        return sum([avg_score*3, avg_aud*2, avg_sales*2])/7


class Genre(models.Model):
    type = models.CharField(max_length=255)


class Movie(models.Model):
    code=models.IntegerField()
    title = models.CharField(max_length=255)
    score = models.FloatField(default=0)
    sales = models.IntegerField()
    normalized_sales = models.FloatField(default=0)
    audience = models.IntegerField()
    normalized_audience = models.FloatField(default=0)
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
    