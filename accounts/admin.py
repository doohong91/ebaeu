from django.contrib import admin
from .models import Profile
from django.contrib.auth import get_user_model


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'nickname', 'description']
    list_display_links = ['user', 'nickname']


@admin.register(get_user_model())
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username']
    list_display_links = ['id', 'username']