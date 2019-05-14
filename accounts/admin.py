from django.contrib import admin
from .models import Profile
from django.contrib.auth import get_user_model

# Register your models here.
admin.site.register(Profile)
admin.site.register(get_user_model())