from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    Class that requests information from the user
    """
    email = models.EmailField('email adress', blank=False, unique=True)
    username = models.CharField(max_length=100, blank=True, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    account_created = models.DateField(auto_now_add=True)


class Post(models.Model):
    title = models.CharField(max_length=100, unique=True, db_index=True)
    slug = models.SlugField(max_length=100, unique=True, db_index=True)
    article_description = models.CharField(max_length=200, null=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_created = models.DateTimeField(auto_now_add=True)
    post_updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='', blank=True, null=True)

    class Meta:
        ordering = ['-post_created']

    def __str__(self):
        return self.title
