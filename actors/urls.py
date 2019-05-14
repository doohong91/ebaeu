from django.urls import path
from . import views

app_name="actors"

urlpatterns = [
    path('',views.index, name="main"),
    path('actors/<int:actor_id>',views.detail, name="detail"),
]
