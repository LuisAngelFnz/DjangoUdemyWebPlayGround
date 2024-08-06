from django.shortcuts import render
from django.views.generic.base import TemplateView

class HomePageView(TemplateView):    
    def get(self, request, *args, **kwargs):
        return render(
            request,
            'core/home.html',
            context={'title':'Home Page'},
            *args,
            **kwargs
        )
        
    
class SamplePageView(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(
            request,
            'core/sample.html',
            context={'title':'Sample Page'},
            *args,
            **kwargs
        )