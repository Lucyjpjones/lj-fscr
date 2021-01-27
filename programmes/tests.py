from django.test import TestCase
from programmes.forms import ProgrammeForm
from programmes.models import Programme
from django.urls import reverse
from django.contrib.auth.models import User
from django.test.client import Client


# form tests
class TestProgrammeForm(TestCase):

    # Checking the correct fields are displayed in the form
    def test_fields_are_explicit_in_form_metaclass(self):
        ''' test correct fields are displayed in the form '''
        form = ProgrammeForm()
        self.assertEqual(form.Meta.fields, '__all__')


# view tests
class TestProgrammeViews(TestCase):
    def setUp(self):
        ''' create superuser, create programme '''
        self.client = Client()
        self.user = User.objects.create_superuser('admin',
                                                  'admin@fscr.com',
                                                  'adminpassword')

        programme = Programme.objects.create(name='test programme')

    def test_get_all_programmes(self):
        ''' test programmes view '''
        response = self.client.get(reverse('programmes'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'programmes/programmes.html')

    def test_get_programme_detail(self):
        ''' test programme detail view '''
        programme = Programme.objects.get(name='test programme')
        response = self.client.get(reverse('programme_detail',
                                           args=(programme.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'programmes/programme_detail.html')

    def test_get_add_programme(self):
        ''' test add programme view, with logged in superuser '''
        self.client.login(username='admin', password='adminpassword')
        response = self.client.get(reverse('add_programme'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'programmes/add_programme.html')

    def test_get_edit_programme(self):
        ''' test edit programme view, with logged in superuser '''
        self.client.login(username='admin', password='adminpassword')
        programme = Programme.objects.get(name='test programme')
        response = self.client.get(reverse('edit_programme',
                                           args=(programme.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'programmes/edit_programme.html')

    def test_sort_programmes_price_asc(self):
        ''' test sort products by price ascending '''
        self.client.login(username='admin', password='adminpassword')
        response = self.client.get('/programmes/?sort=price&direction=asc')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'programmes/programmes.html')

    def test_sort_programmes_price_desc(self):
        ''' test sort products by price descending '''
        response = self.client.get('/programmes/?sort=price&direction=desc')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'programmes/programmes.html')

    def test_sort_programmes_newest(self):
        ''' test sort products by newest first '''
        response = self.client.get('/programmes/?sort=sku&direction=desc')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'programmes/programmes.html')

    def test_sort_programmes_highest_rated(self):
        ''' test sort products by highest rated '''
        response = self.client.get('/programmes/?sort=rating&direction=desc')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'programmes/programmes.html')

    def test_filter_by_cat(self):
        ''' test filter programmes by category rehab '''
        response = self.client.get('/programmes/?category=rehab')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'programmes/programmes.html')
