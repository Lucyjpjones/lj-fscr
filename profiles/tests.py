from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.test.client import Client


class TestProfileViews(TestCase):

    def setUp(self):
        """ create user for tests """
        self.client = Client()
        self.user = User.objects.create_user('david',
                                             'dbeckham@fscr.com',
                                             'userpassword')

    def test_get_profile(self):
        """ test profile view, with logged in user """
        self.client.login(username='david', password='userpassword')
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')
