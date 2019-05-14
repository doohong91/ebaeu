from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Actor, Movie, Genre, Rating
from .serializers import MovieSerializer, ActorSerializer, GenreSerializer, RatingSerializer

def index(request):
  actors = Actor.objects.filter(id__lt=10)
  return render(request,'actors/index.html',{'actors':actors})

def detail(request, actor_id):
  actor = get_object_or_404(Actor,pk=actor_id)
  return render(request,'actors/detail.html',{'actor':actor})
