from django.shortcuts import (render, redirect, reverse,
                              HttpResponse, get_object_or_404)
from django.contrib import messages

from products.models import Product
from programmes.models import Programme


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id, category):
    """ Add a quantity of the specified product to the shopping bag """

    product = get_object_or_404(Product, pk=item_id)
    programme = get_object_or_404(Programme, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {'product': {},
                                      'programme': {}})

    if category == 'product':
        if size:
            if item_id in list(bag.keys()):
                if size in bag[category][item_id]['items_by_size'].keys():
                    bag[category][item_id]['items_by_size'][size] += quantity
                    messages.success(request, (f'Updated size {size.upper()}{product.name} quantity to {bag[category][item_id]["items_by_size"][size]}'))
                else:
                    bag[category][item_id]['items_by_size'][size] = quantity
                    messages.success(request, f'Added size {size.upper()}{product.name} to your bag')
            else:
                bag[category][item_id] = {'items_by_size': {size: quantity}}
                messages.success(request, f'Added size {size.upper()} {product.name} to your bag')
        else:
            if item_id in list(bag.keys()):
                bag[category][item_id] += quantity
                messages.success(request, f'Updated {product.name} quantity to {bag[category][item_id]}')
            else:
                bag[category][item_id] = quantity
                messages.success(request, f'Added {product.name} to your bag')

    elif category == 'programme':
        if item_id in list(bag.keys()):
            bag[category][item_id] += quantity
            messages.success(request, f'Updated {programme.name} quantity to {bag[category][item_id]}')
        else:
            bag[category][item_id] = quantity
            messages.success(request, f'Added {programme.name} to your bag')

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)


def adjust_bag(request, item_id, category):
    """Adjust the quantity of the specified product to the specified amount"""

    product = get_object_or_404(Product, pk=item_id)
    programme = get_object_or_404(Programme, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {'product': {},
                                      'programme': {}})

    if category == 'product':
        if size:
            if quantity > 0:
                bag[category][item_id]['items_by_size'][size] = quantity
                messages.success(request, f'Updated size {size.upper()} {product.name} quantity to {bag[category][item_id]["items_by_size"][size]}')
            else:
                del bag[category][item_id]['items_by_size'][size]
                if not bag[category][item_id]['items_by_size']:
                    del bag[category][item_id]
                messages.success(request, f'Removed size {size.upper()} {product.name} from your bag')
        else:
            if quantity > 0:
                bag[category][item_id] = quantity
                messages.success(request, f'Updated {product.name} quantity to {bag[category][item_id]}')
            else:
                del bag[category][item_id]
                messages.success(request, f'Removed {product.name} from your bag')

    elif category == 'programme':
        if quantity > 0:
            bag[category][item_id] = quantity
            messages.success(request, f'Updated {programme.name} quantity to {bag[category][item_id]}')
        else:
            del bag[category][item_id]
            messages.success(request, f'Removed {programme.name} from your bag')

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id, category):
    """Remove the specified product from bag"""

    product = get_object_or_404(Product, pk=item_id)
    programme = get_object_or_404(Programme, pk=item_id)
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {'product': {},
                                      'programme': {}})

    try:
        if category == 'product':
            if size:
                del bag[category][item_id]['items_by_size'][size]
                if not bag[category][item_id]['items_by_size']:
                    del bag[category][item_id]
                messages.success(request, f'Removed size {size.upper()} {product.name} from your bag')
            else:
                del bag[category][item_id]
                messages.success(request, f'Removed {product.name} from your bag')

        elif category == 'programme':
            del bag[category][item_id]
            messages.success(request, (f'Removed {programme.name} from your bag'))

        request.session['bag'] = bag
        print(request.session['bag'])
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
