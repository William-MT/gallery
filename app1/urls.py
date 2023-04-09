from django.urls import path
from . import views

urlpatterns = [
path('', views.land),
path('home/', views.home),
path('collections/', views.collections),
path('about/', views.about),
]