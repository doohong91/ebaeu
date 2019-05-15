from django.shortcuts import render, get_object_or_404,redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.contrib.auth.decorators import login_required

from .models import Actor, Movie, Genre, Rating
from .serializers import MovieSerializer, ActorSerializer, GenreSerializer, RatingSerializer
from django.contrib.auth import get_user_model

def index(request):
  actors = Actor.objects.filter(id__lt=10)
  return render(request,'actors/index.html',{'actors':actors})

def detail(request, actor_id):
  actor = get_object_or_404(Actor,pk=actor_id)
  return render(request,'actors/detail.html',{'actor':actor})

@login_required  
def like_actor(request, actor_id):
  actor = get_object_or_404(Actor,pk=actor_id)
  if request.user in actor.like_users.all():
    actor.like_users.remove(request.user)
  else:
    actor.like_users.add(request.user)
  return redirect('actors:detail',actor_id)

@login_required  
def viewed_movie(request, actor_id, movie_id):
  movie = get_object_or_404(Movie,pk=movie_id)
  if request.user in movie.viewed_users.all():
    movie.viewed_users.remove(request.user)
  else:
    movie.viewed_users.add(request.user)
  return redirect('actors:detail',actor_id)

@login_required  
def rcmd_movie(request):
  user=request.user
  like_actors=user.like_actors.all()
  return render(request,'actors/recommand.html',{'like_actors':like_actors})