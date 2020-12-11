from django.shortcuts import render, get_object_or_404
from .models import Post


def all_posts(request):
    posts = Post.objects.filter(status=1).order_by('-created_on')

    context = {
        'posts': posts,
    }

    return render (request, 'blog/blog.html', context)


def post_detail(request, slug):
    """ A view to show individual post details """

    post = get_object_or_404(Post, slug=slug)

    context = {
        'post': post,
    }

    return render(request, 'blog/post_detail.html', context)
