from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    avator= models.ImageField(upload_to="avators", default="avator.png")
    background= models.ImageField(upload_to="backgrounds", default="background.jpg")
    following= models.ManyToManyField(User, blank=True, related_name="following")
    bio = models.TextField( default="No bio added")
    created= models.DateTimeField(auto_now_add=True)
    updated= models.DateTimeField(auto_now=True)


    def __str__(self):
        return str(self.user)
        
