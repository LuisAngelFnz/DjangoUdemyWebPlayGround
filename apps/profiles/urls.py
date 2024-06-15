from django.urls import path
from . import views

profiles_urlpatterns = [
    path('',  views.ListProfile.as_view(), name='profile')
]