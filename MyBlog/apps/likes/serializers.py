from .models import Like
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class LikeSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Like
        fields = ['id', 'user', 'post', 'created_at']
        read_only_fields = ['created_at']

class LikeCreateSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Like
        fields = ['user', 'post']

    def validate(self, data):
        user = data.get('user')
        post = data.get('post')
        if Like.objects.filter(user=user, post=post).exists():
            raise serializers.ValidationError("You have already liked this post.")
        return data

    # python manage.py loaddata fixtures/accounts.json