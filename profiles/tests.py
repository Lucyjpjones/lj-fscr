from django.test import TestCase
from profiles.forms import UserProfileForm
from django.urls import reverse
from django.contrib.auth.models import User
from django.test.client import Client


# view tests
class TestProfileViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('david',
                                             'dbeckham@fscr.com',
                                             'userpassword')

    def test_get_profile(self):
        self.client.login(username='david', password='userpassword')
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')
