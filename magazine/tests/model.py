from django.test import TestCase
from magazine.models import Post, Profile, User


class TestAppModel(TestCase):

    def test_model_str(self):
        title = Post.objects.create(title='Django')
        content = Post.objects.create(content='content')
        self.assertEqual(str(title), 'Django')
