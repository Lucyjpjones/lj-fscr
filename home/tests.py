from django.test import TestCase
from django.urls import reverse


# view tests
class TestHomeViews(TestCase):

    def test_get_home(self):
        """ test index view """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')

    def test_get_about(self):
        """ test about view """
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/about.html')

    def test_get_meet_the_coaches(self):
        """ test meet the coaches view """
        response = self.client.get(reverse('meet_the_coaches'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/meet_the_coaches.html')

    def test_get_search(self):
        """ test search view """
        response = self.client.get(reverse('search_results'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/search.html')
