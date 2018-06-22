from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('github/', views.github, name='github'),
    path('github/client/', views.github_client, name='github_client'),
    path('oxford/', views.oxford, name='oxford'),
    path('synonyms/', views.synonyms, name='synonyms'),
    path('chuck/',  views.chuck, name='chuck'),
    path('trivia/', views.trivia, name='trivia'),
    path('weather/', views.weather, name='weather'),
    path('crime/', views.crime, name='crime'),
    path('robohash/', views.robohash, name='robohash')

]
