from django.shortcuts import render
from profiles.models import Profile
from django.views.generic import TemplateView, View
from django.http import JsonResponse
# Create your views here.

def profileview(request):
    
    profile= Profile.objects.get(user= request.user)
    context={
        "profile":profile
    }
    return render(request, "profiles/profile.html", context)

class MyProfile(TemplateView):
    template_name = "profiles/profile.html"


class ProfileData(View):
    def get(self, *args, **kwargs):
        profiled= Profile.objects.get(user=self.request.user)
        profilelist = []
        proposed_list=profiled.get_following_proposal()
        for user in proposed_list:
            p=Profile.objects.get(user__username=user.username)
            profile_item={
                "id":p.id,
                "username":p.user.username,
                "avator":p.avator.url,
            }
            profilelist.append(profile_item)
        return JsonResponse({"prof_data":profilelist})
