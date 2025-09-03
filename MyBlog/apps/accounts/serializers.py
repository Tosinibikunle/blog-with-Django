from .models import customReader, CustomBlogger
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as lazy
from django.contrib.auth.password_validation import validate_password
from django.core.validators import RegexValidator


User = get_user_model()
class CustomBloggerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomBlogger
        fields = ['id', 'email', 'username', 'first_name', 'last_name', 'phone_number', 'date_of_birth', 'bio', 'profile_picture', 'is_verified', 'last_login_ip', 'created_at', 'updated_at']
        read_only_fields = ['is_verified', 'last_login_ip', 'created_at', 'updated_at']

class CustomBloggerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomBlogger
        fields = ['email', 'username', 'first_name', 'last_name', 'phone_number', 'date_of_birth', 'bio', 'profile_picture', 'password']
        extra_kwargs = {
            'password': {'write_only': True, 'required': True, 'validators': [validate_password]},
        }
    def create(self, validated_data):
        user = CustomBlogger.objects.create(
            email=validated_data['email'],
            username=validated_data['username'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            phone_number=validated_data.get('phone_number', None),
            date_of_birth=validated_data.get('date_of_birth', None),
            bio=validated_data.get('bio', ''),
            profile_picture=validated_data.get('profile_picture', None),
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class CustomReaderSerializer(serializers.ModelSerializer):
    user = CustomBloggerSerializer(read_only=True)
    class Meta:
        model = customReader
        fields = ['id', 'user', 'favorite_genres', 'subscribed_newsletter', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']

class CustomReaderCreateSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(queryset=CustomBlogger.objects.all(), source='user', write_only=True)
    class Meta:
        model = customReader
        fields = ['user_id', 'favorite_genres', 'subscribed_newsletter']
    def create(self, validated_data):
        reader = customReader.objects.create(
            user=validated_data['user'],
            favorite_genres=validated_data.get('favorite_genres', ''),
            subscribed_newsletter=validated_data.get('subscribed_newsletter', False),
        )
        reader.save()
        return reader
    def validate_favorite_genres(self, value):
        if value and not all(genre.isalpha() or genre.isspace() or genre == ',' for genre in value):
            raise serializers.ValidationError(lazy("Favorite genres must only contain letters, spaces, and commas."))
        return value
    def validate(self, attrs):
        user = attrs.get('user')
        if customReader.objects.filter(user=user).exists():
            raise serializers.ValidationError(lazy("This user already has a reader profile."))
        return attrs

