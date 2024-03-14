from django.views import generic as baseviews
from django.urls import reverse_lazy
from .models import Page
from .forms import PageForm

# Create your views here.
class PagesListView(baseviews.ListView):
    model = Page

class PageDetailView(baseviews.detail.DetailView):
    model = Page

class PageCreateView(baseviews.CreateView):
    model = Page
    form_class = PageForm
    success_url = reverse_lazy('pages:pages')

class PageUpdateView(baseviews.UpdateView):
    model = Page
    fields = ['title', 'content', 'order']
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse_lazy('pages:update', args=[self.object.id])+'?ok'

class PageDeleteView(baseviews.DeleteView):
    model = Page
    success_url = reverse_lazy('pages:pages')