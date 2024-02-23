from django.urls import path
from .views import article_create_view, article_list_view

urlpatterns = [
    path('create', article_create_view, name='article_create'),
    path('list', article_list_view, name='article_list'),
]