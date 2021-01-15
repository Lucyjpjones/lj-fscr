from django.test import TestCase
from profiles.forms import UserProfileForm


# form tests
class TestUserProfileForm(TestCase):

    # Checking the correct fields are displayed in the form
    def test_fields_are_explicit_in_form_metaclass(self):
        form = UserProfileForm()
