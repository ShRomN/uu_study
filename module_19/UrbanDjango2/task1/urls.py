from django.contrib import admin
from django.urls import path
from task1.views import MainPageView, GamesPageView, CartPageView
from task1.views import sign_up_by_django

urlpatterns = [
    path('', MainPageView.as_view()),
    path('games/', GamesPageView.as_view(), name='games'),
    path('cart/', CartPageView.as_view(), name='cart'),
    path('django_sign_up/', sign_up_by_django, name='sign_up_by_django')
]
