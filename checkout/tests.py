from django.test import TestCase
from checkout.forms import OrderForm


class TestOrderForm(TestCase):

    # Checking required fields

    def test_item_full_name_is_required(self):
        form = OrderForm({'full_name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('full_name', form.errors.keys())
        self.assertEqual(form.errors['full_name'][0],
                         'This field is required.')

    def test_item_email_is_required(self):
        form = OrderForm({'email': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        self.assertEqual(form.errors['email'][0], 'This field is required.')

    def test_item_phone_number_is_required(self):
        form = OrderForm({'phone_number': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('phone_number', form.errors.keys())
        self.assertEqual(form.errors['phone_number'][0],
                         'This field is required.')

    def test_item_country_is_required(self):
        form = OrderForm({'country': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('country', form.errors.keys())
        self.assertEqual(form.errors['country'][0], 'This field is required.')

    def test_item_postcode_is_required(self):
        form = OrderForm({'postcode': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('postcode', form.errors.keys())
        self.assertEqual(form.errors['postcode'][0], 'This field is required.')

    def test_item_town_or_city_is_required(self):
        form = OrderForm({'town_or_city': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('town_or_city', form.errors.keys())
        self.assertEqual(form.errors['town_or_city'][0],
                         'This field is required.')

    def test_item_street_address1_is_required(self):
        form = OrderForm({'street_address1': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('street_address1', form.errors.keys())
        self.assertEqual(form.errors['street_address1'][0],
                         'This field is required.')

    # Checking not required fields

    # Test checkout form for valid data
    # def test_order_form_is_valid(self):
    #     form = OrderForm({
    #         'full_name': 'Lucy Jones',
    #         'email': 'lucy@example.com',
    #         'phone_number': '123456789',
    #         'postcode': 'SW12 9PH',
    #         'town_or_city': 'Furzedown',
    #         'street_address1': 'Street Address 1',
    #         'street_address2': 'Street Address 2',
    #         'county': 'London',
    #         'country': 'United Kingdom',
    #     })

        # self.assertTrue(form.is_valid())

    # def test_order_form_no_data(self):
    #     form = OrderForm(data={})

    #     self.assertFalse(form.is_valid())
    #     self.assertEquals(len(form.errors), 7)
