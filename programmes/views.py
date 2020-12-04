from django.shortcuts import render
from .models import Programme

# Create your views here.


def all_programmes(request):
    """ A view to show all products, including sorting and search queries """

    programmes = Programme.objects.all()

    context = {
        'programmes': programmes,
    }

    return render(request, 'programmes/programmes.html', context)
