from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from registration.models import Profile
from threads.models import Thread

class ListProfile(ListView):
    template_name = 'profiles/profile_list.html'
    model = Profile
    paginate_by = 6

class DetailProfile(DetailView):
    template_name = 'profiles/profile_detail.html'
    model = Profile

    def get_object(self):
        return get_object_or_404(
            Profile, user__username=self.kwargs['username']
        )
    
    def get_context_data(self, *args, **kwargs):
        context = super(DetailProfile, self).get_context_data(
            *args, **kwargs
        )
        threadExist = False
        if not self.request.user.is_anonymous:
            threadExist = bool(Thread.objects.find(
                get_object_or_404(User, username=self.kwargs['username']),
                self.request.user
            ))
        context['threadExist'] = threadExist
        return context