from django.test import TestCase
from products.forms import ProductForm
from products.models import Product, Category
from django.urls import reverse
from django.contrib.auth.models import User
from django.test.client import Client
import unittest


# form tests
class TestProductForm(TestCase):

    # Checking the correct fields are displayed in the form
    def test_fields_are_explicit_in_form_metaclass(self):
        form = ProductForm()
        self.assertEqual(form.Meta.fields, '__all__')


# view tests
class TestProductViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_superuser('admin',
                                                  'admin@fscr.com',
                                                  'adminpassword')

        new_product = Product.objects.create(name='test product', id=2)

    def test_get_all_products(self):
        response = self.client.get(reverse('products'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_get_product_detail(self):
        new_product = Product.objects.get(id=2)
        response = self.client.get(reverse('product_detail', args=(new_product.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_detail.html')

    def test_get_add_product(self):
        self.client.login(username='admin', password='adminpassword')
        response = self.client.get(reverse('add_product'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/add_product.html')

    def test_get_edit_product(self):
        self.client.login(username='admin', password='adminpassword')
        new_product = Product.objects.get(id=2)
        response = self.client.get(reverse('edit_product', args=(new_product.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/edit_product.html')

    def test_can_add_product(self):
        self.client.login(username='admin', password='adminpassword')
        response = self.client.post('/add', {'category': 'Category', 'sku': 'test001', 'name': 'test name', 'colour': 'test colour', 'description': 'test description', 'has_sizes': 'S', 'price': '9.99', 'rating': '5.0', 'image_url': '', 'image': 'test.png'})
        self.assertRedirects(response, reverse('product_detail', {'name': 'test name'}))

    # def test_can_edit_product(self):
    #     self.client.login(username='admin', password='adminpassword')

    # def test_can_delete_product(self):
    #     self.client.login(username='admin', password='adminpassword')
