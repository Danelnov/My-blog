from .models import Post
from .forms import PostForm
from django.utils import timezone
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect


def post_list(request):
    """View to show all posts on the home page"""
    posts = Post.objects.filter(
        published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {"posts": posts})


def post_detail(request, pk: int):
    """View to display the entire post on a separate page

    Args:
        pk (int): the primary key of the post
    """
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    """View to publish a new post"""
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {
        'form': form, 
        "header_title": "New Blog"
        })


def post_edit(request, pk: int):
    """View to edit an old post

    Args:
        pk (int): Primary key of the post to edit
    """
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {
        'form': form, 
        "header_title": f"Edit post: {post.title}"
        })


def author_posts(request, author: str):
    """View to show all posts by a single author

    Args:
        author (str): The author's username
    """
    # Get user, if it does not exist show 404
    author = get_object_or_404(User, username=author)
    # filter user posts
    posts = Post.objects.filter(author=author).filter(
        published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {
        'posts': posts, 
        "header_title": f"{str(author).capitalize()}'s posts"
        })


def posts_by_category(request, category: str):
    """View to show all posts that share a category

    Args:
        category (str): The category name
    """
    # Filter posts by category
    posts = Post.objects.filter(category=category).order_by('-published_date')
    return render(request, 'blog/post_list.html', {
        "posts":posts,
        "header_title": f"Category: {category}",
    })