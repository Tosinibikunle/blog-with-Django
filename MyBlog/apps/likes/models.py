from django.db import models
from django.contrib.auth import get_user_model

    

User = get_user_model()

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('posts.Post', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'post')
        ordering = ['-created_at']
        verbose_name = "like"

    def __str__(self):
        return f"{self.user.email} liked post {self.post.id}"
    
    class User(models.Model):
        email = models.EmailField(unique=True)
        name = models.CharField(max_length=100)

        def __str__(self):
            return self.email
        def get_full_name(self):
            return self.name

