from django.test import TestCase
from bag.templatetags.bag_tools import calc_subtotal
from django.urls import reverse


# bag tools
class TestBagTools(TestCase):

    def test_calc_subtotal(self):
        result = calc_subtotal(2, 5)
        self.assertEqual(10, result)

# bag contexts


# bag views
class TestBagViews(TestCase):

    def test_get_bag(self):
        response = self.client.get(reverse('view_bag'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bag/bag.html')

    # def test_can_add_item(self):
    #     response = self.client.post(reverse('add_to_bag'), {'name': 'Test Item'})
    #     self.assertRedirects(response, '/')

    # def test_can_edit_item(self):

    # def test_can_delete_item(self):

