from django.db import models
from django.contrib.auth.models import User

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Post(models.Model):
    '''
    Blog post, ordered by newest first
    [Code help from 'https://djangocentral.com/building-a-blog-
    application-with-django/']
    '''
    post_type = models.CharField(default='article', max_length=50)
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    references = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    class Meta:
        ordering = ['-created_on']  # Default sort

    def __str__(self):
        return self.title


class Comment(models.Model):
    '''
    Comment on blog post, ordered by newest first
    '''
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return str(self.user)
