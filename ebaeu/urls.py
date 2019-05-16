"""ebaeu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view
from accounts import views as accounts_views
from actors import views as actors_views

schema_view = get_swagger_view(title='Movie API')

urlpatterns = [
    url('api/v1/docs', schema_view),
    path('', actors_views.index, name='main'),
    path('admin/', admin.site.urls),
    path('actors/', include('actors.urls')),
    path('accounts/', include('accounts.urls')),
    path('@<str:username>/', accounts_views.profile, name='profile'),
]
