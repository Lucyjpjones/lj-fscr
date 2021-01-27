from django.test import TestCase
from blog.forms import CommentForm
from blog.models import Post
from django.urls import reverse
from django.contrib.auth.models import User
from django.test.client import Client


# form tests
class TestCommentForm(TestCase):

    def test_item_body_is_required(self):
        ''' test body field is required '''
        form = CommentForm({'body': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('body', form.errors.keys())
        self.assertEqual(form.errors['body'][0],
                         'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        ''' test correct fields are displayed in the form '''
        form = CommentForm()
        self.assertEqual(form.Meta.fields, ['body'])


# view tests
class TestBlogViews(TestCase):
    def setUp(self):
        ''' create user '''
        self.client = Client()
        self.user = User.objects.create_user('david',
                                             'dbeckham@fscr.com',
                                             'userpassword')

    def test_get_all_posts(self):
        ''' test blog view, with logged in user '''
        self.client.login(username='david', password='userpassword')
        response = self.client.get(reverse('blog'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blog.html')

    def test_get_post_detail(self):
        ''' test post detail view, with logged in user '''
        self.client.login(username='david', password='userpassword')
        new_post = Post.objects.create(slug='test', author=self.user,
                                       image='test.png')
        response = self.client.get(reverse('post_detail', args=(
                                   new_post.slug,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_detail.html')

    def test_sort_posts_newest(self):
        ''' test sort posts by created on date '''
        self.client.login(username='david', password='userpassword')
        response = self.client.get('/blog/?sort=created_on&direction=desc')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blog.html')

    def test_sort_posts_alph_asc(self):
        ''' test sort posts by title alphabetically ascending '''
        self.client.login(username='david', password='userpassword')
        response = self.client.get('/blog/?sort=title&direction=asc')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blog.html')

    def test_sort_posts_alph_desc(self):
        ''' test sort posts by title alphabetically descending '''
        self.client.login(username='david', password='userpassword')
        response = self.client.get('/blog/?sort=title&direction=desc')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blog.html')
