from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404
from registration.models import Profile
from threads.models import Thread

class ListProfile(ListView):
    template_name = 'profiles/profile_list.html'
    model = Profile
    paginate_by = 3

    def get_queryset(self, *args, **kwargs):
        querySet = super(ListProfile, self).get_queryset(
            *args, **kwargs
        )

        return  querySet.exclude(
            user__username=self.request.user.username
        )


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
        print(context)
        threadExist = Thread.objects.filter(
            users__username=[self.request.user.username, self.kwargs['username']]
        ).count() > 0
        context['threadExist'] = threadExist

        return context