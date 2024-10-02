from django.urls import path
from .views import ThreadList, ThreadDetail
threads_urlpatters = [
    path('', ThreadList.as_view(), name='threadList'),
    path('thread/<int:pk>', ThreadDetail.as_view(), name='threaDetail')
]