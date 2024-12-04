from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexView, name='index'),
    path('<str:room>/', views.roomView, name='room'),
    path('checkview', views.checkView, name='check')
]