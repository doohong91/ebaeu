from django.urls import path,include
from . import views

app_name = "accounts"

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('delete/', views.delete, name='delete'),
    path('profile/<int:user_id>/', views.profile, name='profile'),
    path('change_profile/<int:user_id>/', views.change_profile, name='change_profile'),
    path('follow/', views.follow, name='follow'),
]
