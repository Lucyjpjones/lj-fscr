from django.shortcuts import render, get_object_or_404
from .models import Programme

# Create your views here.


def all_programmes(request):
    """ A view to show all programmes, including sorting and search queries """

    programmes = Programme.objects.all()

    context = {
        'programmes': programmes,
    }

    return render(request, 'programmes/programmes.html', context)


def programme_detail(request, programme_id):
    """ A view to show individual programme details """

    programme = get_object_or_404(Programme, pk=programme_id)

    context = {
        'programme': programme,
    }

    return render(request, 'programmes/programme_detail.html', context)
