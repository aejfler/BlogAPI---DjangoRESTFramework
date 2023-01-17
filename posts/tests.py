from django.test import TestCase

from django.contrib.auth.models import User

from .models import Post


class BlogTests(TestCase):

    # creating a user
    @classmethod
    def setUpTestData(cls):
        user1 = User.objects.create_user(username='testuser', password='testpassword')
        user1.save()

    # creating blog post
        post1 = Post.objects.create(author=user1, title='Test blog title', content='This is a body content...')
        post1.save()

    def test_blog_contents(self):
        post = Post.objects.get(id=1)
        author = f'{post.author}'
        title = f'{post.title}'
        content = f'{post.content}'

        self.assertEqual(author, 'testuser')
        self.assertEqual(title, 'Test blog title')
        self.assertEqual(content, 'This is a body content...')
