from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse, Http404
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, TemplateView

from .models import Thread, Message

@method_decorator(login_required, name='dispatch')
class ThreadList(TemplateView):
    template_name = 'threads/thread_list.html'

@method_decorator(login_required, name='dispatch')
class ThreadDetail(DetailView):
    model = Thread

def addMessage(request, pk):
    response = {'created':False}
    if not request.user.is_authenticated:
        raise Http404('Usuario no autenticado')
    
    if request.method != 'GET':
        raise Http404('Metodo no permitido')
    
    content = request.GET.get('content')
    if content:
        thread = get_object_or_404(Thread, pk=pk)
        message = Message.objects.create(user=request.user, content=content)
        thread.messages.add(message)
        response['created'] = True
        if thread.messages.count() == 1:
            response['first'] = True

    return JsonResponse(response)

@login_required
def startThread(request, username):
    user = get_object_or_404(User, username=username)
    thread = Thread.objects.findOrCreate(user, request.user)
    return redirect(reverse_lazy('threads:detail', args=[thread.pk]))

