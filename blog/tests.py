from django.test import TestCase
from blog.forms import CommentForm
from blog.models import Post
from django.urls import reverse
from blog.forms import CommentForm
from django.contrib.auth.models import User
from django.test.client import Client
import unittest


# form tests
class TestCommentForm(TestCase):

    # Checking required fields
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
class TestBlogViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('david',
                                             'dbeckham@fscr.com',
                                             'userpassword')

    def test_get_all_posts(self):
        self.client.login(username='david', password='userpassword')
        response = self.client.get(reverse('blog'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blog.html')

    def test_get_post_detail(self):
        self.client.login(username='david', password='userpassword')
        new_post = Post.objects.create(slug='test', author=self.user, image='test.png')
        response = self.client.get(reverse('post_detail', args=(new_post.slug,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_detail.html')

    # def test_can_add_comment(self):
    #     self.client.login(username='david', password='userpassword')
    #     response = self.client.post('post_detail', {'body': 'test comment'})
    #     self.assertRedirects(response, 'blog/blog.html')


    # # def test_toggle_references(self)
