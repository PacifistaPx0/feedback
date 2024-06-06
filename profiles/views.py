from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.views.generic import ListView


from .models import UserProfile

# Create your views here.


class CreatedProfileView(CreateView):
    template_name = "profiles/create_profile.html"
    model = UserProfile
    fields = "__all__"
    success_url = "/profiles"

class ProfileListView(ListView):
    template_name = "profiles/profile_list.html"
    model = UserProfile
    context_object_name = "profiles"
