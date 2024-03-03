from django.views.generic import ListView,CreateView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from .models import Page

# Create your views here.
class PagesListView(ListView):
    model = Page

class PageDetailView(DetailView):
    model = Page

class PageCreateView(CreateView):
    model = Page
    fields = ['title', 'content', 'order']
    success_url = reverse_lazy('pages:pages')