from django.contrib import admin
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter
from .models import Genre, Movie, Rating, Actor


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'score', 'normalized_audience', 'normalized_sales', 'open_date']
    list_display_links = ['id', 'title']
    list_filter = (('open_date', DateRangeFilter),)
    search_fields = ['title', ]


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'get_point']
    list_display_links = ['id', 'name']
    search_fields = ['name', ]


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['id', 'type']
    list_display_links = ['id', 'type']
    
    
@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ['id', 'score', 'comment']
    list_display_links = ['id', 'score']


# admin.site.register(Youtube)
