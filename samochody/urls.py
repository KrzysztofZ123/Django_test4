from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('duze/', views.duze, name='duze'),
    path('srednie/', views.srednie, name='srednie'),
    path('male/', views.male, name='male'),
]
