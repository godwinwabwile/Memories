from django.urls import path
from profiles.views import profileview, ProfileData, MyProfile

app_name= "profiles"


urlpatterns=[
    path("", MyProfile.as_view(), name="myprofile"),
    path("myprofjson/", ProfileData.as_view(), name="profjson"),
]