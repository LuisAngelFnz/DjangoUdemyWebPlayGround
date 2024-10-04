from django.views.generic import ListView, DetailView
from django.views.generic import TemplateView

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import Thread

@method_decorator(login_required, name='dispatch')
class ThreadList(ListView):
    # template_name = 'templates/thread_list.html'
    model = Thread
    def get_queryset(self):
        querySet = super().get_queryset()
        return querySet.filter(users=self.request.user)

@method_decorator(login_required, name='dispatch')
class ThreadDetail(DetailView):
    model = Thread