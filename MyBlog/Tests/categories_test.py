from django.test import TestCase
from ..apps.categories.models import Category, Tag


class CategoryModelTest(TestCase):
    def setup(self):
        self.category = Category.objects.create(name="Django", slug="django")

    def test_category_creation(self):
        assert self.category.name == "Django"
        assert self.category.slug == "django"
        assert str(self.category) == "Django"
        assert str(self.category.slug) == "django"

    def test_get_absolute_url(self):
        url = self.category.get_absolute_url()
        assert url == f"/categories/{self.category.slug}/"

    def test_get_posts_empty(self):
        posts = self.category.get_posts()
        assert posts.count() == 0

    def test_get_post_count(self):
        count = self.category.get_post_count()
        assert count == 0

class TagModelTest(TestCase):
    def setup(self):
        self.tag = Tag.objects.create(name="Python", slug="python")

    def test_tag_creation(self):
        assert self.tag.name == "Python"
        assert self.tag.slug == "python"
        assert str(self.tag) == "Python"
        assert str(self.tag.slug) == "python"

    def test_get_absolute_url(self):
        url = self.tag.get_absolute_url()
        assert url == f"/tags/{self.tag.slug}/"

    def test_get_posts_empty(self):
        posts = self.tag.get_posts()
        assert posts.count() == 0

    def test_get_post_count(self):
        count = self.tag.get_post_count()
        assert count == 0
# Note: The actual URL patterns (like "/categories/<slug>/") should match your project's URL configuration.