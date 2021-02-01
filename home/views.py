from django.shortcuts import render, redirect, reverse
from blog.models import Post
from products.models import Product
from programmes.models import Programme
from django.db.models import Q
from django.contrib import messages
from itertools import chain
from .forms import ContactForm
from django.core.mail import send_mail
from profiles.models import UserProfile


def index(request):
    """
    A view to return the index page
    """
    posts = Post.objects.filter(status=1).order_by('-created_on')[:2]

    # Pre populate fields with profile information
    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        form = ContactForm(initial={
                    'contact_name': profile.default_full_name,
                    'contact_email': profile.default_email,
        })
    else:
        form = ContactForm()

    context = {
        'posts': posts,
        'form': form,
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
            messages.warning(request,
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


def contact_us(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():

            sender_name = form.cleaned_data['contact_name']
            sender_email = form.cleaned_data['contact_email']
            sender_query = form.cleaned_data['query']
            sender_message = form.cleaned_data['message']

            # Email template
            message = ("Name: {0}\nEmail: {1}\n\nMessage:\n{2}".format
                       (sender_name, sender_email, sender_message))
            send_mail(sender_query, message, sender_email,
                      ['lucyjpjones@gmail.com'])

            messages.success(request, "Message sent!")

    return redirect(reverse("home"))
