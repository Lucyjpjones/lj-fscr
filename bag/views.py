from django.shortcuts import (render, redirect, reverse,
                              HttpResponse, get_object_or_404)
from django.contrib import messages

from products.models import Product
from programmes.models import Programme


def view_bag(request):
    """
    A view that renders the bag contents page
    """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id, category):
    """
    Adds a quantity of the specified item to the bag, distinguishes
    the category of the item, then checks if the item_id already exists
    in the bag. If item is a product it will also check for size. If
    the item exists the quantity will be incremented, otherwise the
    item will be added to the bag
    [Code taken from Code Institute and modified for personal use]
    """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {'product': {},
                                      'programme': {}})

    if category == 'product':
        product = get_object_or_404(Product, pk=item_id)
        if size:
            if item_id in list(bag[category].keys()):
                if size in bag[category][item_id]['items_by_size'].keys():
                    bag[category][item_id]['items_by_size'][size] += quantity
                    messages.success(request, (
                     f'Updated size {size.upper()} {product.name} quantity '
                     f'to {(bag[category][item_id]["items_by_size"][size])}'))
                else:
                    bag[category][item_id]['items_by_size'][size] = quantity
                    messages.success(request,
                                     f'Added size {size.upper()}'
                                     f'{product.name} to your bag')
            else:
                bag[category][item_id] = {'items_by_size': {size: quantity}}
                messages.success(request,
                                 f'Added size {size.upper()}'
                                 f'{product.name} to your bag')
        else:
            if item_id in list(bag[category].keys()):
                bag[category][item_id] += quantity
                messages.success(request,
                                 f'Updated {product.name} quantity to '
                                 f'{bag[category][item_id]}')
            else:
                bag[category][item_id] = quantity
                messages.success(request, f'Added {product.name} to your bag')

    elif category == 'programme':
        programme = get_object_or_404(Programme, pk=item_id)
        if item_id in list(bag[category].keys()):
            bag[category][item_id] += quantity
            messages.success(request,
                             f'Updated {programme.name} quantity to '
                             f'{bag[category][item_id]}')
        else:
            bag[category][item_id] = quantity
            messages.success(request, f'Added {programme.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id, category):
    """
    Adjusts the quantity of the specified item to the specified amount,
    if user enters quantity over 99 the user will get an error message for
    invalid value, if user enters 0 the item will be removed from the bag
    [Code taken from Code Institute and modified for personal use]
    """

    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {'product': {},
                                      'programme': {}})

    if category == 'product':
        product = get_object_or_404(Product, pk=item_id)
        if size:
            if quantity in range(1, 99):
                bag[category][item_id]['items_by_size'][size] = quantity
                messages.success(request, (
                 f'Updated size {size.upper()} {product.name} quantity '
                 f'to {(bag[category][item_id]["items_by_size"][size])}'))
            elif quantity > 99:
                messages.error(request, "Value must be less than or equal \
                                to 99")
            else:
                del bag[category][item_id]['items_by_size'][size]
                if not bag[category][item_id]['items_by_size']:
                    del bag[category][item_id]
                messages.success(request,
                                 f'Removed size {size.upper()}'
                                 f'{product.name} from your bag')
        else:
            if quantity in range(1, 99):
                bag[category][item_id] = quantity
                messages.success(request,
                                 f'Updated {product.name} '
                                 f'quantity to {bag[category][item_id]}')
            elif quantity > 99:
                messages.error(request, "Value must be less than or equal \
                                to 99")
            else:
                del bag[category][item_id]
                messages.success(request,
                                 f'Removed {product.name} '
                                 f'from your bag')

    elif category == 'programme':
        programme = get_object_or_404(Programme, pk=item_id)
        if quantity in range(1, 99):
            bag[category][item_id] = quantity
            messages.success(request,
                             f'Updated {programme.name} '
                             f'quantity to {bag[category][item_id]}')
        elif quantity > 99:
            messages.error(request, "Value must be less than or equal \
                                to 99")
        else:
            del bag[category][item_id]
            messages.success(request,
                             f'Removed {programme.name} '
                             f'from your bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id, category):
    """
    Remove the specified item from bag
    """

    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {'product': {},
                                      'programme': {}})

    try:
        if category == 'product':
            product = get_object_or_404(Product, pk=item_id)
            if size:
                del bag[category][item_id]['items_by_size'][size]
                if not bag[category][item_id]['items_by_size']:
                    del bag[category][item_id]
                messages.success(request,
                                 f'Removed size {size.upper()} '
                                 f'{product.name} from your bag')
            else:
                del bag[category][item_id]
                messages.success(request,
                                 f'Removed {product.name} from your bag')

        elif category == 'programme':
            programme = get_object_or_404(Programme, pk=item_id)
            del bag[category][item_id]
            messages.success(request,
                             f'Removed {programme.name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
