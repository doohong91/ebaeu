# Error list

## 1. 개요

애로사항을 겪었던 에러를 모았다.

## 2. Error

`django.db.utils.IntegrityError: FOREIGN KEY constraint failed`

- JSON을 loaddata할 때 JSON 안에 model에 없는 FOREIGN KEY가 있을 때 발생
  - FOREIGN KEY에 해당하는 model을 먼저 JSON을 import 하거나 JSON에 있는 model에는 없는 FOREIGN KEY 값을 제거해야함

`django.core.serializers.base.DeserializationError: Problem installing fixture 'C:\...': 'ManyToManyRel' object has no bute 'to_python'`

- ManyToManyField가 없는 model에 JSON을 loaddata할 때 발생
  - ManyToManyField가 선언된 model에 import 되어야 함

## 3. api
*actors/urls.py*
```python
from django.urls import path
from . import views

app_name="actors"

urlpatterns = [
    path('',views.index, name="main"),
    path('detail/',views.detail, name="detail"),
    path('actors/',views.actor_list),
    path('actors/<int:actor_id>/',views.actor_detail),
    path('actors/<int:actor_id>/rating/',views.rating_list),
    path('genres/',views.genre_list),
    path('movies/',views.movie_list),
    path('rating/<int:rating_id>',views.rating_detail),
]
```

*actors/views.py*
```python
from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Actor, Movie, Genre, Rating
from .serializers import MovieSerializer, ActorSerializer, GenreSerializer, RatingSerializer

def index(request):
  return render(request,'actors/index.html')

def detail(request):
  return render(request,'actors/detail.html')

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
```

*ebaeu/urls.py*
```python
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view
from accounts import views as accounts_views

schema_view = get_swagger_view(title='Movie API')

urlpatterns = [
    url('api/v1/docs', schema_view),
    path('admin/', admin.site.urls),
    path('api/v1/', include('actors.urls')),
    path('accounts/', include('accounts.urls')),
    path('<str:username>/', accounts_views.profile, name='profile'),
]
```