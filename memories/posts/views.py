from multiprocessing import context
from django.shortcuts import render
from .models import Post

# Create your views here.

def home(request):
    qs= Post.objects.all()
    topic= "django"
    description= "Django is a good framework that builds powerful sites"

    context={
        "qs":qs,
        "topic": topic,
         "description":description
    }

    return render(request, "posts/main.html", context)