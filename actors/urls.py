from django.urls import path
from . import views

app_name="actors"

urlpatterns = [
    path('',views.index, name="main"),
    path('actors/<int:actor_id>',views.detail, name="detail"),
    path('actors/<int:actor_id>/like',views.like_actor, name="like"),
    path('actors/<int:movie_id>',views.viewed_movie, name="watched"),
    path('recommand',views.rcmd_movie,name="recommand")
]
