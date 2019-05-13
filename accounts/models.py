from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.

class User(AbstractUser):
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name="followings")

class Profile(models.Model):
    description = models.TextField(blank=True) 
    nickname = models.CharField(max_length=30,blank=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    # def __str__(self):
    #     return f"<{self.user.username}의 프로필, nickname: {self.nickname}, description: {self.description}>"