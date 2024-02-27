from django.urls import path
from . import views

urlpatterns = [
    path('', views.PagesListView.as_view(), name='pages'),
    path('<int:pk>/<slug:slug>/', views.PageDetail.as_view(), name='page'),
]