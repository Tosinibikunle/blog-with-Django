from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def post(self):
        return self.content[:30]

    def author_name(self):
        return self.author.name

    def author_email(self):
        return self.author.email

    def author_id(self):
        return self.author.id

    def posts(self):
        return Post.objects.filter(author=self.author)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
