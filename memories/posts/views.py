from django.shortcuts import render

# Create your views here.

def home(request):
    topic= "Django"
    description= "Django is an amazing web framework"

    return render(request, "posts/main.html", {"topic": topic, "description":description})