from django.urls import path
from . import views

profiles_urlpatterns = [
    path('',  views.ListProfile.as_view(), name='profiles'),
    path('detail/<slug:username>/',  views.DetailProfile.as_view(), name='detail')
]