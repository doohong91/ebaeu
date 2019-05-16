from django.urls import path
from . import views

app_name="actors"

urlpatterns = [
    path('',views.index, name="main"),
    path('<int:actor_id>',views.detail, name="detail"),
    path('<int:actor_id>/like', views.like_actor, name="like"),
    path('recommand/movie/',views.recommand_movie, name="recommand_movie"),
    path('recommand/actor/',views.recommand_actor, name="recommand_actor"),
    path('viewed/<int:movie_id>',views.viewed_movie, name="viewed_movie"),
    path('<int:actor_id>/rating/', views.create_rating, name="create_rating"),
    path('<int:actor_id>/rating/<int:rating_id>/', views.update_rating, name="update_rating"),
    path('<int:actor_id>/rating/<int:rating_id>/delete/', views.delete_rating, name="delete_rating"),
]
