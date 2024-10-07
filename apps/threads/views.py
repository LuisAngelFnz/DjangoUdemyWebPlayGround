from django.views.generic import DetailView
from django.views.generic import TemplateView
from django.http import JsonResponse, Http404
from django.shortcuts import get_object_or_404

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import Thread,Message

@method_decorator(login_required, name='dispatch')
class ThreadList(TemplateView):
    template_name = 'templates/thread_list.html'

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

    return JsonResponse(response)