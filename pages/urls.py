from django.urls import path
from . import views

pages_urlpatterns = [
    path('', views.PagesListView.as_view(), name='pages'),
    path('<int:pk>/<slug:slug>', views.PageDetailView.as_view(), name='page'),
    path('create/', views.PageCreateView.as_view(), name='create'),
    path('update/<int:pk>/', views.PageUpdateView.as_view(), name='update')
]