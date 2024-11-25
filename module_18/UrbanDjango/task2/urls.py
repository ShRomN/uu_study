from django.contrib import admin
from django.urls import path
from task2.views import func_view
from task2.views import ClassView

urlpatterns = [
    path('func_view/', func_view, name='func_view'),
    path('class_view/', ClassView.as_view(), name='class_view')
]
