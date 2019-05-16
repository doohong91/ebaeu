from django.shortcuts import render, get_object_or_404,redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Case, When, F
from .models import Actor, Movie, Genre, Rating
from .forms import RatingForm, ActorForm
# from .serializers import MovieSerializer, ActorSerializer, GenreSerializer, RatingSerializer
from django.http import HttpResponseRedirect
from django.views.decorators.http import require_POST
from django.contrib.auth import get_user_model


def index(request):
  sort = request.GET.get('sort')
  if not sort:
    sort = 2017
  actors = Actor.objects.annotate(
    movie_count=Count(
      Case(
        When(movies__open_date__year__in = range(int(sort), 2020), then=F('movies'))
      )
    )
  ).filter(movie_count__gte=3)
  actors = sorted(actors, key=lambda x:x.get_point, reverse=True)[:10]
  return render(request,'actors/index.html', {'actors': actors, 'years': range(2010, 2020)})


def search(request):
  query = request.GET.get('q')
  if query:
    actors = Actor.objects.filter(name__icontains = query)
    return render(request,'actors/index.html', {'actors': actors})
  else:
    return redirect('main')


def detail(request, actor_id):
  actor = get_object_or_404(Actor,pk=actor_id)
  return render(request,'actors/detail.html', {'actor':actor, 'form': RatingForm()})


@login_required  
def like_actor(request, actor_id):
  actor = get_object_or_404(Actor,pk=actor_id)
  if request.user in actor.like_users.all():
    actor.like_users.remove(request.user)
  else:
    actor.like_users.add(request.user)
  return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required  
def viewed_movie(request, movie_id):
  movie = get_object_or_404(Movie,pk=movie_id)
  if request.user in movie.viewed_users.all():
    movie.viewed_users.remove(request.user)
  else:
    movie.viewed_users.add(request.user)
  return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required  
def recommand_movie(request):
  user=request.user
  like_actors=user.like_actors.all()
  return render(request,'actors/recommandMovie.html',{'like_actors':like_actors})


@login_required
def recommand_actor(request):
  viewed_movies=request.user.viewed_movies.all()
  return render(request,'actors/recommandActor.html',{'viewed_movies':viewed_movies})
  
  
@login_required
@require_POST
def create_rating(request, actor_id):
  form = RatingForm(request.POST)
  if form.is_valid():
    rating = form.save(commit=False)
    rating.user = request.user
    rating.actor_id = actor_id
    rating.save()
  return redirect('actors:detail', actor_id)
  
  
@login_required
def update_rating(request, actor_id, rating_id):
  rating = get_object_or_404(Rating, id=rating_id)
  if request.method == 'POST':
    if rating.user == request.user:
      form = RatingForm(request.POST, instance=rating)
      if form.is_valid():
        form.save()
    return redirect('actors:detail', actor_id)
  else:
    form = RatingForm(instance=rating)
    actor = get_object_or_404(Actor,pk=actor_id)
    return render(request,'actors/detail.html',{'actor':actor, 'form': form})


@login_required
@require_POST
def delete_rating(request, actor_id, rating_id):
  rating = get_object_or_404(Rating, id=rating_id)
  if rating.user == request.user:
    rating.delete()
  return redirect('actors:detail', actor_id)


@staff_member_required
def create_actor(request):
  if request.method == 'POST':
    form = ActorForm(require_POST)
    if form.is_valid():
      form.save()
    return redirect('main')
  else:
    form = ActorForm()
    return render(request, 'actors/form.html', {'form': form, 'name': '등록'})


@staff_member_required
def edit_actor(request, actor_id):
  actor = get_object_or_404(Actor, id=actor_id)
  if request.method == 'POST':
    form = ActorForm(request.POST, instance=actor)
    if form.is_valid():
      form.save()
    return redirect('actors:detail', actor_id)
  else:
    form = ActorForm(instance=actor)
    return render(request, 'actors/form.html', {'form': form, 'name': '수정'})
