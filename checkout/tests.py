from django.test import TestCase
from checkout.forms import OrderForm
from checkout.models import Order, OrderLineItem, ProgOrderLineItem


class TestOrderForm(TestCase):

    # forms

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

    # Checking the correct fields are displayed in the form
    def test_fields_are_explicit_in_form_metaclass(self):
        form = OrderForm()
        self.assertEqual(form.Meta.fields, ['full_name', 'email', 'phone_number', 'street_address1', 'street_address2', 'town_or_city', 'postcode', 'country', 'county'])
    