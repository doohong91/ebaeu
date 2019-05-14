from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="followings")
    like_actor = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_user')
    viewed_movie = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='viewed_user')


class Profile(models.Model):
    description = models.TextField(default='자기소개') 
    nickname = models.CharField(max_length=30, default='닉네임')
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"<{self.user.username}의 프로필, nickname: {self.nickname}, description: {self.description}>"