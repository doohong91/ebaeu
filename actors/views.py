from django.shortcuts import render, get_object_or_404,redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.contrib.auth.decorators import login_required

from .models import Actor, Movie, Genre, Rating
from .serializers import MovieSerializer, ActorSerializer, GenreSerializer, RatingSerializer

def index(request):
  actors = Actor.objects.filter(id__lt=10)
  return render(request,'actors/index.html',{'actors':actors})

def detail(request, actor_id):
  actor = get_object_or_404(Actor,pk=actor_id)
  return render(request,'actors/detail.html',{'actor':actor})

def like_actor(request, actor_id):
  actor = get_object_or_404(Actor,pk=actor_id)
  if request.user in actor.like_users.all():
    actor.like_users.remove(request.user)
  else:
    actor.like_users.add(request.user)
  return redirect('actors:detail',actor_id)