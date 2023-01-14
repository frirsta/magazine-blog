from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField


class User(AbstractUser):
    """
    Class that requests information from the user
    """
    email = models.EmailField('email adress', blank=False, unique=True)
    username = models.CharField(max_length=100, blank=True, unique=True)
    account_created = models.DateField(auto_now_add=True)
    USERNAME_FIELD = 'username'


class Post(models.Model):
    title = models.CharField(max_length=50, unique=True, db_index=True)
    slug = models.SlugField(max_length=50, unique=True, db_index=True)
    article_description = models.CharField(max_length=100, null=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_created = models.DateTimeField(auto_now_add=True)
    post_updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='', blank=False, null=True)

    class Meta:
        ordering = ['-post_created']

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    image = CloudinaryField(
        'static/img',
        default='https://res.cloudinary.com/magazine-blog/image/upload/v1672740868/static/img/default-profile.8c3e2b017043.png')
    bio = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.user.username


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=300)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_created = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=True)

    class Meta:
        ordering = ('comment_created',)

    def __str__(self):
        return 'Comment by {}'.format(self.user)
