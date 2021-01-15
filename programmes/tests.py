from django.test import TestCase
from programmes.forms import ProgrammeForm
from programmes.models import Programme
from django.urls import reverse
from django.contrib.auth.models import User
from django.test.client import Client
import unittest


# form tests
class TestProgrammeForm(TestCase):

    # Checking the correct fields are displayed in the form
    def test_fields_are_explicit_in_form_metaclass(self):
        form = ProgrammeForm()
        self.assertEqual(form.Meta.fields, '__all__')


# view tests
class TestProgrammeViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_superuser('admin',
                                                  'admin@fscr.com',
                                                  'adminpassword')

        new_programme = Programme.objects.create(name='test programme', id=2)

    def test_get_all_programmes(self):
        response = self.client.get(reverse('programmes'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'programmes/programmes.html')

    def test_get_programme_detail(self):
        new_programme = Programme.objects.get(id=2)
        response = self.client.get(reverse('programme_detail', args=(new_programme.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'programmes/programme_detail.html')

    def test_get_add_programme(self):
        self.client.login(username='admin', password='adminpassword')
        response = self.client.get(reverse('add_programme'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'programmes/add_programme.html')

    def test_get_edit_programme(self):
        self.client.login(username='admin', password='adminpassword')
        new_programme = Programme.objects.get(id=2)
        response = self.client.get(reverse('edit_programme', args=(new_programme.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'programmes/edit_programme.html')
