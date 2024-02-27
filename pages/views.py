from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import Page

# Create your views here.
class PagesListView(ListView):
    model = Page

class PageDetail(DetailView):
    model = Page