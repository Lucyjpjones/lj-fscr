from django.test import TestCase
from bag.templatetags.bag_tools import calc_subtotal
from django.urls import reverse


# tools test
class TestBagTools(TestCase):

    def test_calc_subtotal(self):
        result = calc_subtotal(2, 5)
        self.assertEqual(10, result)


# view tests
class TestBagViews(TestCase):

    def test_get_bag(self):
        response = self.client.get(reverse('view_bag'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bag/bag.html')
