from django.views import generic as bv
from django.urls import reverse_lazy
# from django.shortcuts import redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from .models import Page
from .forms import PageForm

    
@method_decorator(staff_member_required, name='dispatch')
class PagesListView(bv.ListView):
    model = Page

@method_decorator(staff_member_required, name='dispatch')
class PageDetailView(bv.detail.DetailView):
    model = Page

@method_decorator(staff_member_required, name='dispatch')
class PageCreateView(bv.CreateView):
    model = Page
    form_class = PageForm
    success_url = reverse_lazy('pages:pages')

@method_decorator(staff_member_required, name='dispatch')   
class PageUpdateView(bv.UpdateView):
    model = Page
    form_class = PageForm
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse_lazy('pages:update', args=[self.object.id])+'?ok'

@method_decorator(staff_member_required, name='dispatch')
class PageDeleteView(bv.DeleteView):
    model = Page
    success_url = reverse_lazy('pages:pages')