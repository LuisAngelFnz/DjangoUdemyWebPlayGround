from django.shortcuts import render
from django.views.generic import ListView, DetailView
from registration.models import Profile

class ListProfile(ListView):
    template_name = 'profiles/profile_list.html'
    model = Profile
