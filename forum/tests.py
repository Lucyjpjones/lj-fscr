from django.test import TestCase
from forum.forms import CommentForm, ThreadForm
from forum.models import Thread
from django.urls import reverse
from django.contrib.auth.models import User
from django.test.client import Client
from django.template.defaultfilters import slugify


# form tests
class TestCommentForm(TestCase):

    def test_item_topic_is_required(self):
        form = ThreadForm({'topic': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('topic', form.errors.keys())
        self.assertEqual(form.errors['topic'][0],
                         'This field is required.')

    def test_item_description_is_required(self):
        form = ThreadForm({'description': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('description', form.errors.keys())
        self.assertEqual(form.errors['description'][0],
                         'This field is required.')

    def test_item_body_is_required(self):
        form = CommentForm({'body': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('body', form.errors.keys())
        self.assertEqual(form.errors['body'][0],
                         'This field is required.')

    # Checking the correct fields are displayed in the form
    def test_fields_are_explicit_in_form_metaclass(self):
        form = CommentForm()
        self.assertEqual(form.Meta.fields, ['body'])


# view tests
class TestForumViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('david',
                                             'dbeckham@fscr.com',
                                             'userpassword')

    def test_get_all_threads(self):
        self.client.login(username='david', password='userpassword')
        response = self.client.get(reverse('forum'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'forum/forum.html')

    def test_get_thread_detail(self):
        self.client.login(username='david', password='userpassword')
        new_thread = Thread.objects.create(slug='test', author=self.user)
        response = self.client.get(reverse('thread_detail', args=(
                                           new_thread.slug,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'forum/thread_detail.html')

    def test_get_add_thread(self):
        self.client.login(username='david', password='userpassword')
        response = self.client.get(reverse('add_thread'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'forum/add_thread.html')

    def test_get_edit_thread(self):
        self.client.login(username='david', password='userpassword')
        new_thread = Thread.objects.create(id='1', author=self.user)
        response = self.client.get(reverse('edit_thread', args=(
                                            new_thread.slug,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'forum/edit_thread.html')

    def test_thread_has_slug(self):
        """Threads are given slugs correctly when saving"""
        thread = Thread.objects.create(topic="My first thread")
        thread.author = self.user
        thread.save()
        self.assertEqual(thread.slug, slugify(thread.topic))
