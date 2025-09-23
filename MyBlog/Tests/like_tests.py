from django.test import TestCase
from apps.likes.models import Like, User
from apps.posts.models import Post

class LikeModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(email="testuser@example.com", name="Test User")
        self.post = Post.objects.create(title="Test Post", content="Test Content", author=self.user)
        self.like = Like.objects.create(user=self.user, post=self.post)
    def test_like_creation(self):
        self.assertEqual(self.like.user, self.user)
        self.assertEqual(self.like.post, self.post)
    def test_like_str(self):
        self.assertEqual(str(self.like), f"{self.user.email} liked post {self.post.id}")
        
