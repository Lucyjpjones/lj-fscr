# https://djangocentral.com/building-a-blog-application-with-django/

from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True, null=True)
    slug = models.SlugField(max_length=200, unique=True, null=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='forum_posts', null=True)
    content = models.TextField(null=True)
    created_on = models.DateField(auto_now_add=True, null=True)
    status = models.IntegerField(choices=STATUS, default=1)

    class Meta:
        ordering = ['-created_on']  # Default sort

    def __str__(self):
        return self.title

    # https://stackoverflow.com/questions/45847278/django-use-slugify-for-detail-url
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        return super(Post, self).save(*args, **kwargs)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='comments', null=True)
    name = models.CharField(max_length=80, null=True)
    body = models.CharField(max_length=300, null=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)
