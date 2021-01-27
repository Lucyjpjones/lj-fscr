from django.test import TestCase
from bag.templatetags.bag_tools import calc_subtotal
from django.urls import reverse
from products.models import Product
from programmes.models import Programme


# tools test
class TestBagTools(TestCase):

    def test_calc_subtotal(self):
        result = calc_subtotal(2, 5)
        self.assertEqual(10, result)


# view tests
class TestBagViews(TestCase):

    def setUp(self):
        product = Product.objects.create(name='test product', id=1,
                                         has_sizes=True, price=5.99)
        programme = Programme.objects.create(name='test programme', id=2,
                                             price=40.00)

    def test_get_bag(self):
        response = self.client.get(reverse('view_bag'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bag/bag.html')

    def test_add_product_to_bag(self):
        product = Product.objects.get(name='test product')
        post_data = {
            'quantity': '1',
            'redirect_url': '/'
        }
        response = self.client.post(reverse(
                                'add_to_bag',
                                kwargs={'item_id': product.id, 'category':
                                        'product'}),
                                    data=post_data)
        self.assertRedirects(response, '/')

    # def test_add_sized_product_to_bag(self):
    #     product = Product.objects.get(name='test product')
    #     size = 'M'
    #     post_data = {
    #         'quantity': '1',
    #         'redirect_url': '/'
    #     }
    #     response = self.client.post(reverse(
    #                             'add_to_bag',
    #                             kwargs={'item_id': product.id,
    #                                     'category': 'product'}),
    #                                 data=post_data)
    #     self.assertRedirects(response, '/')


    def test_add_programme_to_bag(self):
        programme = Programme.objects.get(name='test programme')
        post_data = {
            'quantity': '1',
            'redirect_url': '/'
        }
        response = self.client.post(reverse(
                                'add_to_bag',
                                kwargs={'item_id': programme.id, 'category':
                                        'programme'}),
                                    data=post_data)
        self.assertRedirects(response, '/')

    def test_adjust_quantity_in_bag(self):
        product = Product.objects.get(name='test product')
        post_data = {
            'quantity': '1',
            'redirect_url': '/'
        }
        self.client.post(reverse(
                         'add_to_bag',
                         kwargs={'item_id': product.id, 'category':
                                 'product'}), data=post_data)

        post_data_new = {
            'quantity': '4',
        }
        response = self.client.post(reverse(
                                    'adjust_bag',
                                    kwargs={'item_id': product.id, 'category':
                                            'product'}), data=post_data_new)

        self.assertRedirects(response, '/bag/')

    def test_remove_item_from_bag(self):
        product = Product.objects.get(name='test product')
        post_data = {
            'quantity': '1',
            'redirect_url': '/'
        }
        self.client.post(reverse(
                         'add_to_bag',
                         kwargs={'item_id': product.id, 'category':
                                 'product'}), data=post_data)

        response = self.client.post(reverse(
                                'remove_from_bag',
                                kwargs={'item_id': product.id, 'category':
                                        'product'}))

        self.assertEqual(response.status_code, 200)
