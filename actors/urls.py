from django.urls import path
from . import views

app_name="actors"

urlpatterns = [
    path('',views.index, name="main"),
    path('actors/<int:actor_id>',views.detail, name="detail"),
    path('actors/', views.search, name="search"),
    path('actors/<int:actor_id>/like', views.like_actor, name="like"),
    path('actors/<int:actor_id>/<int:movie_id>/',views.viewed_in_detail, name="viewed_in_detail"),
    path('recommand',views.rcmd_movie,name="recommand"),
    path('recommand/<int:movie_id>',views.viewed_in_recommand, name="viewed_in_recommand"),
    path('actors/<int:actor_id>/rating/', views.create_rating, name="create_rating"),
    path('actors/<int:actor_id>/rating/<int:rating_id>/', views.update_rating, name="update_rating"),
    path('actors/<int:actor_id>/rating/<int:rating_id>/delete/', views.delete_rating, name="delete_rating"),
]
