from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexView, name='index'),
    path('chat/<str:room>/', views.roomView, name='room'),
    path('checkview', views.checkView, name='checkview'),
    path('send', views.send, name='send')
]