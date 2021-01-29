from django.shortcuts import render, redirect, reverse
from blog.models import Post
from products.models import Product
from programmes.models import Programme
from profiles.models import UserProfile
from django.db.models import Q
from django.contrib import messages
from itertools import chain


def index(request):
    """
    A view to return the index page
    """
    posts = Post.objects.filter(status=1).order_by('-created_on')[:2]

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        first_name = profile.default_full_name.split(" ")[0]
        last_name = profile.default_full_name.split(" ")[1]
    else:
        profile = ''
        first_name = ''
        last_name = ''


    context = {
        'posts': posts,
        'profile': profile,
        'first_name': first_name,
        'last_name': last_name,
    }

    return render(request, 'home/index.html', context)


def search_results(request):
    """
    A view to return the search page
    Creates empty list, if query in get request redirects user to
    search page with filtered results, if no query submitted redirects
    user to search view with error message
    """

    query = None
    results_list = ()
    filtered_products = Product.objects.filter(discontinued=False)
    filtered_programmes = Programme.objects.filter(discontinued=False)
    filtered_posts = Post.objects.filter(status=1)

    if 'q' in request.GET:
        query = request.GET['q']
        if not query:
            messages.error(request,
                           "You didn't enter any search criteria!")
            return redirect(reverse('search_results'))

        products = filtered_products.filter(Q(name__icontains=query) | Q(
                                        description__icontains=query))
        programmes = filtered_programmes.filter(Q(
            name__icontains=query) | Q(description__icontains=query))
        posts = filtered_posts.filter(Q(title__icontains=query))

        results_list = list(chain(products, programmes, posts))

    context = {
        'search_term': query,
        'results_list': results_list,
    }

    return render(request, 'home/search.html', context)


def about(request):
    """
    A view to return the about page
    """

    return render(request, 'home/about.html')


def meet_the_coaches(request):
    """
    A view to return the coaches page
    """

    return render(request, 'home/meet_the_coaches.html')
