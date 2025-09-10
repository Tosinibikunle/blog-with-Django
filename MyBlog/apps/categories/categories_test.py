from django.test import TestCase
from .models import Category





class CategoryModelTest(TestCase):
    def setup(self):
        self.category = Category.objects.create(name="Django", slug="django")

    def test_category_creation(self):
        assert self.category.name == "Django"
        assert self.category.slug == "django"
        assert str(self.category) == "Django"
        assert str(self.category.slug) == "django"
