from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Lower
from .models import Programme, Category
from .forms import ProgrammeForm


def all_programmes(request):
    """
    A view to show all programmes, including sorting and filtering by
    category name
    """

    programmes = Programme.objects.filter(discontinued=False)
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                programmes = programmes.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            programmes = programmes.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            programmes = programmes.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

    current_sorting = f'{sort}_{direction}'

    context = {
        'programmes': programmes,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'programmes/programmes.html', context)


def programme_detail(request, programme_id):
    """ A view to show individual programme details """

    programme = get_object_or_404(Programme, pk=programme_id)

    context = {
        'programme': programme,
        'on_page': True,
    }

    return render(request, 'programmes/programme_detail.html', context)


@login_required
def add_programme(request):
    """
    If logged in as superuser can add a new programme to the store
    Gets programme form, if user input is valid, saves programme and redirects
    user to the programme detail page
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProgrammeForm(request.POST, request.FILES)
        if form.is_valid():
            programme = form.save()
            messages.success(request, 'Successfully added programme!')
            return redirect(reverse('programme_detail', args=[programme.id]))
        else:
            messages.error(request, 'Failed to add programme. Please ensure \
                the form is valid.')
    else:
        form = ProgrammeForm()

    template = 'programmes/add_programme.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_programme(request, programme_id):
    """
    If logged in as superuser can edit a programme in the store
    Gets programme form by programme id, if user input is valid, updates
    programme form and redirects user to the programme detail page
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    programme = get_object_or_404(Programme, pk=programme_id)
    if request.method == 'POST':
        form = ProgrammeForm(request.POST, request.FILES, instance=programme)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated programme!')
            return redirect(reverse('programme_detail', args=[programme.id]))
        else:
            messages.error(request, 'Failed to update programme. Please ensure \
                the form is valid.')
    else:
        form = ProgrammeForm(instance=programme)
        messages.info(request, f'You are editing {programme.name}')

    template = 'programmes/edit_programme.html'
    context = {
        'form': form,
        'programme': programme,
    }

    return render(request, template, context)


@login_required
def delete_programme(request, programme_id):
    """
    If logged in as superuser can delete a programme in the store
    Gets programme form by programme id, changes discontinued field to
    True and saves programme - Programme is removed from view but is
    still available in admin
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    programme = get_object_or_404(Programme, pk=programme_id)
    programme.discontinued = True
    programme.save()
    messages.success(request, 'Programme deleted!')
    return redirect(reverse('programmes'))
