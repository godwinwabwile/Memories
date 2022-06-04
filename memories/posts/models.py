from django.db import models
from django.contrib.auth.models import User
from profiles.models import Profile 

# Create your models here.

class Post(models.Model):
    picture= models.ImageField(upload_to="images", blank=True, )
    body= models.TextField()
    liked= models.ManyToManyField(User, blank=True, default=None)
    author= models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="posts")
    updated= models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.pk)

    def get_liked(self):
        return self.liked.all()

    @property
    def liked_count(self):
        return self.liked.all().count()
