from django.test import TestCase
from products.forms import ProductForm
from products.models import Product
from django.urls import reverse
from django.contrib.auth.models import User
from django.test.client import Client


# form tests
class TestProductForm(TestCase):

    def test_fields_are_explicit_in_form_metaclass(self):
        ''' test correct fields are displayed in the form '''
        form = ProductForm()
        self.assertEqual(form.Meta.fields, '__all__')


# view tests
class TestProductViews(TestCase):
    def setUp(self):
        """ create superuser and product for tests """
        self.client = Client()
        self.user = User.objects.create_superuser('admin',
                                                  'admin@fscr.com',
                                                  'adminpassword')

        product = Product.objects.create(name='test product')

    def test_get_all_products(self):
        """ test products view """
        response = self.client.get(reverse('products'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_get_product_detail(self):
        """ test product detail view """
        product = Product.objects.get(name='test product')
        response = self.client.get(reverse('product_detail',
                                           args=(product.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_detail.html')

    def test_get_add_product(self):
        """ test add product view, with logged in superuser """
        self.client.login(username='admin', password='adminpassword')
        response = self.client.get(reverse('add_product'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/add_product.html')

    def test_get_edit_product(self):
        """ test edit product view, with logged in superuser """
        self.client.login(username='admin', password='adminpassword')
        product = Product.objects.get(name='test product')
        response = self.client.get(reverse('edit_product',
                                           args=(product.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/edit_product.html')

    def test_can_add_product(self):
        """ test can add product successfully """
        self.client.login(username='admin', password='adminpassword')
        form_data = {'name': 'test product', 'colour': 'test colour',
                     'price': 4.99}
        response = self.client.post(reverse(
                                'add_product'),
                                    data=form_data)
        self.assertEqual(response.status_code, 200)

    def test_sort_products_price_asc(self):
        """ test sort products by price ascending """
        response = self.client.get('/products/?sort=price&direction=asc')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_sort_products_price_desc(self):
        """ test sort products by price descending """
        response = self.client.get('/products/?sort=price&direction=desc')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_sort_products_newest(self):
        """ test sort products by newest first """
        response = self.client.get('/products/?sort=sku&direction=desc')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_sort_products_highest_rated(self):
        """ test sort products by highest rated """
        response = self.client.get('/products/?sort=rating&direction=desc')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_filter_by_cat(self):
        """ test filter products by category new arrivals """
        response = self.client.get('/products/?category=new_arrivals')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')
