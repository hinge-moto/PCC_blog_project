from django.shortcuts import render

from .models import BlogPost


def index(request):
    """The home page for Blog Project."""
    return render(request, 'blogs/index.html')


def post_titles(request):
    """Show all blog post titles."""
    titles = BlogPost.objects.order_by('date_added')
    context = {'titles': titles}
    return render(request, 'blogs/post_titles.html', context)