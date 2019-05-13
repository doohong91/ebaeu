from django.contrib import admin
from .models import Genre,Movie,Rating,Actor
# Register your models here.
admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(Rating)
# admin.site.register(Youtube)
admin.site.register(Actor)
