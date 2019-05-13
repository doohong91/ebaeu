from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Actor, Movie, Genre, Rating
from .serializers import MovieSerializer, ActorSerializer, GenreSerializer, RatingSerializer

def index(request):
  return render(request,'actors/index.html')

# Create your views here.
@api_view(['GET'])
def actor_list(request):
  actors = Actor.objects.all()
  serializer = ActorSerializer(actors, many=True)
  return Response(serializer.data)


@api_view(['GET'])
def actor_detail(request, actor_id):
  try:
    actor = get_object_or_404(Actor, pk=actor_id)
    serializer = ActorSerializer(actor)
    return Response(serializer.data)
  except:
    return Response({"message": "HTTP_404_NOT_FOUND"},status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def genre_list(request):
  genre = Genre.objects.all()
  serializer = GenreSerializer(genre, many=True)
  return Response(serializer.data)

@api_view(['GET'])
def movie_list(request):
  movies = Movie.objects.all()
  serializer = MovieSerializer(movies, many=True)
  return Response(serializer.data)

@api_view(['GET','POST'])
def rating_list(request,actor_id):
  try:
    actor = get_object_or_404(Actor,pk=actor_id)
  except:
    return Response({"message": "HTTP_404_NOT_FOUND"},status=status.HTTP_404_NOT_FOUND)

  if request.method == 'GET':
    ratings=actor.rating.all()
    serializer=RatingSerializer(ratings,many=True)
    return Response(serializer.data)
  elif request.method == 'POST':
    serializer=RatingSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save(actor=actor)
      return Response({"message": "작성되었습니다."})
    return Response({"message": "HTTP_400_BAD_REQUEST"},status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def rating_detail(request,rating_id):
  try:
    rating = get_object_or_404(Rating,pk=rating_id)
  except:
    return Response({"message": "HTTP_404_NOT_FOUND"},status=status.HTTP_404_NOT_FOUND)
  if request.method == 'GET':
    serializer=RatingSerializer(rating)
    return Response(serializer.data)
  elif request.method == 'PUT':
    serializer=RatingSerializer(rating, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response({"message": "수정되었습니다."})
    return Response({"message": "HTTP_400_BAD_REQUEST"},status=status.HTTP_400_BAD_REQUEST)
  elif request.method == 'DELETE':
    rating.delete()
    return Response({"message": "삭제되었습니다."})