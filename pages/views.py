from django.views import generic as bv
from django.urls import reverse_lazy
from django.shortcuts import redirect
from .models import Page
from .forms import PageForm

class StaffRequiredMix(object):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            print('Entrada no autorizada retornando a login')
            return redirect(reverse_lazy('admin:login'))
        return super().dispatch(request, *args, **kwargs)
    
# Create your views here.
class PagesListView(StaffRequiredMix, bv.ListView):
    model = Page

class PageDetailView(StaffRequiredMix, bv.detail.DetailView):
    model = Page

class PageCreateView(StaffRequiredMix, bv.CreateView):
    model = Page
    form_class = PageForm
    success_url = reverse_lazy('pages:pages')
    
class PageUpdateView(StaffRequiredMix, bv.UpdateView):
    model = Page
    form_class = PageForm
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse_lazy('pages:update', args=[self.object.id])+'?ok'

class PageDeleteView(bv.DeleteView):
    model = Page
    success_url = reverse_lazy('pages:pages')