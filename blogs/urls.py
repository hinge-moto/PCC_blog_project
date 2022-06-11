"""Defines URL patterns for blogs."""

from django.urls import path

from . import views

app_name = 'blogs'
urlpatterns = [
    # Home page.
    path('', views.index, name='index'),
    # Page that shows all blog post titles.
    path('post_titles/', views.post_titles, name='post_titles'),
]