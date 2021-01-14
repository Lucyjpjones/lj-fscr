from django.test import TestCase
from bag.templatetags.bag_tools import calc_subtotal
from bag.contexts import bag_contents


# bag tools
class TestBagTools(TestCase):

    def test_calc_subtotal(self):
        result = calc_subtotal(2, 5)
        self.assertEqual(10, result)

# bag contexts



# bag views
