from django.db import models
from django.utils.text import slugify

class Article(models.Model):
    CATEGORY_CHOICES = [
        ("tech", "Technology"),
        ("lifestyle", "Lifestyle"),
        ("business", "Business"),
        ("news", "News"),
    ]

    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)  # Ensure unique slugs
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # For edits
    thumb = models.ImageField(default='default.png', blank=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, blank=True)
    is_published = models.BooleanField(default=True)  # For filtering in search/archive
    views = models.PositiveIntegerField(default=0)  # Track number of views
    likes = models.PositiveIntegerField(default=0)  # Track number of likes

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50] + "..." if len(self.body) > 50 else self.body

    def save(self, *args, **kwargs):
        # Auto-generate slug from title if not set
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
