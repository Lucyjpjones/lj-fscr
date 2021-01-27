from django.test import TestCase
from checkout.forms import OrderForm
from django.urls import reverse
from products.models import Product
from programmes.models import Programme


# view tests
class TestCheckoutViews(TestCase):

    def setUp(self):
        ''' create product and programme '''
        product = Product.objects.create(name='test product',
                                         price=5.99)
        programme = Programme.objects.create(name='test programme',
                                             price=40.00)

    def test_get_checkout(self):
        ''' test checkout view '''
        product = Product.objects.get(name='test product')
        programme = Programme.objects.get(name='test programme')
        session = self.client.session
        session['bag'] = {'product': {product.id: 1},
                          'programme': {programme.id: 1}}
        session.save()
        response = self.client.get(reverse('checkout'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout.html')

    def test_checkout_success(self):
        ''' test checkout success '''
        product = Product.objects.get(name='test product')
        programme = Programme.objects.get(name='test programme')
        session = self.client.session
        session['bag'] = {'product': {product.id: 1},
                          'programme': {programme.id: 1}}
        session.save()
        post_data = {
            'full_name': 'test user',
            'email': 'test@test.com',
            'phone_number': '123245789',
            'street_address1': 'test street',
            'street_address2': '',
            'town_or_city': 'test city',
            'county': 'test county',
            'country': 'GB',
            'postcode': '12345',
            'client_secret': 'client_1_secret_1',
        }

        response = self.client.post(reverse('checkout'),
                                    data=post_data, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout_success.html')


# form tests
class TestOrderForm(TestCase):
    ''' test full name field is required '''
    def test_item_full_name_is_required(self):
        form = OrderForm({'full_name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('full_name', form.errors.keys())
        self.assertEqual(form.errors['full_name'][0],
                         'This field is required.')

    def test_item_email_is_required(self):
        ''' test email field is required '''
        form = OrderForm({'email': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        self.assertEqual(form.errors['email'][0], 'This field is required.')

    def test_item_phone_number_is_required(self):
        ''' test number field is required '''
        form = OrderForm({'phone_number': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('phone_number', form.errors.keys())
        self.assertEqual(form.errors['phone_number'][0],
                         'This field is required.')

    def test_item_country_is_required(self):
        ''' test country field is required '''
        form = OrderForm({'country': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('country', form.errors.keys())
        self.assertEqual(form.errors['country'][0], 'This field is required.')

    def test_item_postcode_is_required(self):
        ''' test postcode field is required '''
        form = OrderForm({'postcode': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('postcode', form.errors.keys())
        self.assertEqual(form.errors['postcode'][0], 'This field is required.')

    def test_item_town_or_city_is_required(self):
        ''' test town/city field is required '''
        form = OrderForm({'town_or_city': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('town_or_city', form.errors.keys())
        self.assertEqual(form.errors['town_or_city'][0],
                         'This field is required.')

    def test_item_street_address1_is_required(self):
        ''' test street address 1 field is required '''
        form = OrderForm({'street_address1': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('street_address1', form.errors.keys())
        self.assertEqual(form.errors['street_address1'][0],
                         'This field is required.')
