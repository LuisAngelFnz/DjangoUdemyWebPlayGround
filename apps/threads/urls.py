from django.urls import path
from .views import ThreadList, ThreadDetail, addMessage, startThread

threads_urlpatters = [
    path('', ThreadList.as_view(), name='list'),
    path('thread/<int:pk>', ThreadDetail.as_view(), name='detail'),
    path('thread/<int:pk>/addMessage', addMessage, name='addMessage'),
    path('thread/startThread/<username>', startThread, name='startThread')
]