from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404
from registration.models import Profile

class ListProfile(ListView):
    template_name = 'profiles/profile_list.html'
    model = Profile

class DetailProfile(DetailView):
    template_name = 'profiles/profile_detail.html'
    model = Profile

    def get_object(self) -> Profile:
        return get_object_or_404(
            Profile, user__username=self.kwargs['username']
        )