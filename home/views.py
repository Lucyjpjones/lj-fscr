from django.shortcuts import render, redirect, reverse, get_object_or_404
from blog.models import Post
from products.models import Product
from programmes.models import Programme
from django.db.models import Q
from django.contrib import messages
from itertools import chain


def index(request):
    """ A view to return the index page """

    posts = Post.objects.filter(status=1).order_by('-created_on')[:2]
    context = {
        'posts': posts,
    }

    return render(request, 'home/index.html', context)


def search_results(request):
    """ A view to return the search page """

    # search bar queries
    query = None

    if 'q' in request.GET:
        query = request.GET['q']
        if not query:
            messages.error(request,
                           "You didn't enter any search criteria!")
            return redirect(reverse('search_results'))

        products = Product.objects.filter(Q(name__icontains=query) | Q(
                                        description__icontains=query))
        programmes = Programme.objects.filter(Q(name__icontains=query) | Q
                                               (description__icontains=query))
        posts = Post.objects.filter(Q(title__icontains=query))

        results_list = list(chain(products, programmes, posts))

    context = {
        'prducts': products,
        'programmes': programmes,
        'posts': posts,
        'search_term': query,
        'results_list': results_list,
    }

    return render(request, 'home/search.html', context)


def about(request):
    """ A view to return the about page """

    return render(request, 'home/about.html')


def meet_the_coaches(request):
    """ A view to return the coaches page """

    return render(request, 'home/meet_the_coaches.html')
