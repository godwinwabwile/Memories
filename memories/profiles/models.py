from django.db import models
from django.contrib.auth.models import User
from itertools import chain
import random

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

    def get_posts(self):
        '''get posts queryset'''
        return self.posts.all()

    @property
    def num_posts(self):
        '''get count of total posts'''
        return self.posts.all().count()

    '''following queryset'''
    def get_following_qs(self):
        return self.following.all()

    '''following list'''
    def get_following_list(self):
        following_list = [p for p in self.get_following_qs()]
        return following_list
    
    '''count of people we are following'''
    @property
    def following_count(self):
        return self.get_following_qs().count()

    '''function that gets the followers of a given user'''
    def get_followers(self):
        profs= Profile.objects.all()
        followers_list=[]
        for profile in profs:
            if self.user in profile.get_following_qs():
                followers_list.append(profile)
        return followers_list

    '''function to get the number of people that follow the user'''
    @property
    def number_followers(self):
        return len(self.get_followers())

    def get_my_and_following_posts(self):
        users=[users for users in self.get_following_qs()] #get users that i am following
        posts_list=[]
        qs=None

        for u in users:
            prof=Profile.objects.get(user=u) #fetch a given user's profile
            prof_posts=prof.posts.all() #fetch the posts of a given user
            posts_list.append(prof_posts)  #adding all posts of the user to the posts list

        my_posts = self.posts.all() #get all off my posts
        posts_list.append(my_posts) #adding my posts to the posts list


        if len(posts_list)> 0:
            qs=sorted(chain(*posts_list), reverse=True, key=lambda obj: obj.created)
        return qs


    def get_following_proposal(self):
        profs= Profile.objects.all().exclude(user=self.user)
        followers_list= [p for p in self.get_following_qs()]
        available = [p.user for p in profs if p.user not in followers_list]
        random.shuffle(available)
        return available[:3]





    

        
