from rest_framework import serializers
from .models import Movie, Genre, Actor, Rating


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = [
            'id',
            'comment',
            'score',
        ]

# class YoutubeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Youtube
#         fields = [
#             'id',
#             'link',
#         ]


class MovieSerializer(serializers.ModelSerializer):
    # youtube = YoutubeSerializer(many=True)

    class Meta:
        model = Movie
        fields = [
            'id',
            'code',
            'title',
            'score',
            'audience',
            'poster_URL',
            'actors',
            'sales',
            'genres',
            'summary',
        ]


class ActorSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many=True)
    ratings = RatingSerializer(many=True)
    average = serializers.SerializerMethodField('scoresAverage')

    def scoresAverage(self, obj):
        length = obj.ratings.count()
        if length != 0:
            total = 0
            for rating in obj.ratings.all():
                total += rating.score
            result = round(total/length, 2)
        else:
            result = 0
        return result

    class Meta:
        model = Actor
        fields = [
            'id',
            'name',
            'image',
            'ratings',
            'average',
            'movies'
        ]


class GenreSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many=True)

    class Meta:
        model = Genre
        fields = [
            'id',
            'type',
            'movies'
        ]
