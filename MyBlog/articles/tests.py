from django.test import TestCase
from .models import Article


# Create your tests here.
class ArticleModelTest(TestCase):
    def setUp(self):
        self.article = Article.objects.create(
            title="Test Article",
            body="This is a test article body.",
            category="tech"
        )

    def test_article_creation(self):
        self.assertEqual(self.article.title, "Test Article")
        self.assertEqual(self.article.body, "This is a test article body.")
        self.assertEqual(self.article.category, "tech")
        self.assertTrue(self.article.is_published)
        self.assertEqual(self.article.views, 0)
        self.assertEqual(self.article.likes, 0)

    def test_snippet_method(self):
        snippet = self.article.snippet()
        self.assertEqual(snippet, "This is a test article body....")
