from django.urls import include, path
from app424 import views

urlpatterns = [
    path('add/', views.add, name='add'),
    path('', views.list, name='list'),
]

