"""Defines URL patterns for blogs."""

from django.urls import path

from . import views

app_name = 'blogs'
urlpatterns = [
    # Home page.
    path('', views.index, name='index'),
    # Page that shows all blog post titles.
    path('post_titles/', views.post_titles, name='post_titles'),
    # Page that displays a single blog post.
    path('post_titles/<int:post_id>/', views.post, name='post'),
    # Page for adding a new blog post.
    path('new_post/', views.new_post, name='new_post'),
    # Page for editing a post.
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
]