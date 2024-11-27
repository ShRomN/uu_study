from django.contrib import admin
from django.urls import path
from task3.views import MainPageView, MoviesPageView, FavoritesPageView

urlpatterns = [
    path('', MainPageView.as_view()),
    path('movies/', MoviesPageView.as_view(), name='movies'),
    path('favorites/', FavoritesPageView.as_view(), name='favorites')
]
