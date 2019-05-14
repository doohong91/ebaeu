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
