# сюда мы будем добавлять наши URL соотношения по мере разработки сайта

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]