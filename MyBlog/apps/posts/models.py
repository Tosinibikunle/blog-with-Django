from django.db import models
from django.contrib.auth import get_user_model




User = get_user_model()

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    def post(self):
        return self.content[:30]  # Return first 30 characters of content
    def author_name(self):
        return self.author.name  # Assuming User model has a 'name' field
    def author_email(self):
        return self.author.email  # Assuming User model has an 'email' field
    def author_id(self):
        return self.author.id  # Assuming User model has an 'id' field