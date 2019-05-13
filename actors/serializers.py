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
            'score_aud',
            'score_cri',
            'score_net',
            'audience',
            'poster_URL',
            'actors',
            'sales'
            'genres',
            'summary',
        ]


class ActorSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(many=True)
    rating = RatingSerializer(many=True)
    class Meta:
        model = Actor
        fields = [
            'id',
            'name',
            'image_URL',
            'movie',
            'rating'
        ]


class GenreSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(many=True)

    class Meta:
        model = Genre
        fields = [
            'id',
            'type',
            'movie'
        ]



