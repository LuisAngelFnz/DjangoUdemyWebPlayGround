from django.urls import path
from .views import ThreadList, ThreadDetail, addMessage

threads_urlpatters = [
    path('', ThreadList.as_view(), name='list'),
    path('thread/<int:pk>', ThreadDetail.as_view(), name='detail'),
    path('thread/<int:pk>/addMessage', addMessage, name='addMessage')
]