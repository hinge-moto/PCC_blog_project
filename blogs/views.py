from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import BlogPost
from .forms import PostForm


def index(request):
    """The home page for Blog Project."""
    return render(request, 'blogs/index.html')


def post_titles(request):
    """Show all blog post titles."""
    titles = BlogPost.objects.filter(owner=request.user).order_by('date_added')
    context = {'titles': titles}
    return render(request, 'blogs/post_titles.html', context)


def post(request, post_id):
    """Show a single blog post."""
    title = BlogPost.objects.get(id=post_id)
    post = BlogPost.objects.get(id=post_id).text
    context = {'post': post, 'title': title}
    return render(request, 'blogs/post.html', context)


@login_required
def new_post(request):
    """Add a new post."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = PostForm()
    else:
        # POST data submitted; process data.
        form = PostForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:post_titles')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'blogs/new_post.html', context)


@login_required
def edit_post(request, post_id):
    """Edit a post."""
    post = BlogPost.objects.get(id=post_id)

    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = PostForm(instance=post)
    else:
        # POST data submitted; process data.
        form = PostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:post', post_id=post.id)

    context = {'post': post, 'form': form}
    return render(request, 'blogs/edit_post.html', context)