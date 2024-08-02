from django.urls import path
from .views import *
urlpatterns = [
    path('movie_list/', movie_list, name='movie_list'), 
    path('movie_details/<int:pk>/', movie_details, name='movie_details'),
]