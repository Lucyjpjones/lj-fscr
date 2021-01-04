from django.shortcuts import render
from blog.models import Post


def index(request):
    """ A view to return the index page """

    posts = Post.objects.filter(status=1).order_by('-created_on')[:2]
    context = {
        'posts': posts,
    }

    return render(request, 'home/index.html', context)


def about(request):
    """ A view to return the about page """

    return render(request, 'home/about.html')


def meet_the_coaches(request):
    """ A view to return the coaches page """

    return render(request, 'home/meet_the_coaches.html')
