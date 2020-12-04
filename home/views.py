from django.shortcuts import render


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def meet_the_coaches(request):
    """ A view to return the coaches page """

    return render(request, 'home/meet_the_coaches.html')
