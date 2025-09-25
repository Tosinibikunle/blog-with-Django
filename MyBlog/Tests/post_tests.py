from django.test import TestCase
from apps.posts.models import Post
from apps.accounts.models import CustomBlogger, customReader
from django.contrib.auth import get_user_model

User = get_user_model()

class PostModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.post = Post.objects.create(title='Test Post', content='Test Content', author=self.user)
        self.blogger = CustomBlogger.objects.create(user=self.user, username='testblogger', bio='Test Bio')
        self.reader = customReader.objects.create(user=self.user, favorite_genres='Fiction, Mystery', subscribed_newsletter=True)
    def test_post_creation(self):
        self.assertEqual(self.post.title, 'Test Post')
        self.assertEqual(self.post.content, 'Test Content')
        self.assertEqual(self.post.author.username, 'testuser')
        self.assertIsNotNone(self.post.created_at)
    def test_blogger_profile(self):
        self.assertEqual(self.blogger.username, 'testblogger')
        self.assertEqual(self.blogger.bio, 'Test Bio')
        self.assertFalse(self.blogger.is_verified)    
