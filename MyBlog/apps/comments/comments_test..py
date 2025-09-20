from django.test import TestCase
from .models import Comment
from django.contrib.auth import get_user_model
from apps.posts.models import Post

User = get_user_model()

class CommentModelTest(TestCase):

    def setUp(self):
       
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.post = Post.objects.create(title='Test Post', content='Test Content', author=self.user)

    def test_comment_creation(self):
        comment = Comment.objects.create(user=self.user, post=self.post, content='Test Comment')
        self.assertEqual(comment.user, self.user)
        self.assertEqual(comment.post, self.post)
        self.assertEqual(comment.content, 'Test Comment')
        self.assertIsNotNone(comment.created_at)
