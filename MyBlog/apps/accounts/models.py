from django.db import models
from django.utils.translation import gettext_lazy as lazy
from django.core.validators import RegexValidator
from django.conf import settings


class CustomBlogger(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="blogger_profile",
    )
    first_name = models.CharField(
        max_length=30, null=True, blank=True, verbose_name=lazy("first name")
    )
    last_name = models.CharField(
        max_length=30, null=True, blank=True, verbose_name=lazy("last name")
    )
    username = models.CharField(
        max_length=30, unique=True, verbose_name=lazy("username")
    )
    email = models.EmailField(lazy("email address"), unique=True)
    phone_number = models.CharField(
        max_length=15,
        unique=True,
        null=True,
        blank=True,
        validators=[
            RegexValidator(r"^\+?1?\d{9,15}$", lazy("Enter a valid phone number."))
        ],
        verbose_name=lazy("phone number"),
    )
    date_of_birth = models.DateField(
        null=True, blank=True, verbose_name=lazy("date of birth")
    )
    bio = models.TextField(null=True, blank=True, verbose_name=lazy("biography"))
    profile_picture = models.ImageField(
        upload_to="profile_pics/",
        null=True,
        blank=True,
        verbose_name=lazy("profile picture"),
    )
    is_verified = models.BooleanField(default=False, verbose_name=lazy("is verified"))
    last_login_ip = models.GenericIPAddressField(
        null=True, blank=True, verbose_name=lazy("last login IP address")
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=lazy("account created at")
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name=lazy("account updated at")
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    class Meta:
        verbose_name = lazy("user")
        verbose_name_plural = lazy("users")

    def __str__(self):
        return self.email

    def get_full_name(self):
        full_name = f"{self.first_name} {self.last_name}"
        return full_name.strip() or self.email

    def get_short_name(self):
        return self.first_name or self.email

    def verify_account(self):
        self.is_verified = True
        self.save(update_fields=["is_verified"])

    def update_last_login_ip(self, ip_address):
        self.last_login_ip = ip_address
        self.save(update_fields=["last_login_ip"])


class customReader(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="reader_profile",
    )
    favorite_genres = models.CharField(
        max_length=255, null=True, blank=True, verbose_name=lazy("favorite genres")
    )
    subscribed_newsletter = models.BooleanField(
        default=False, verbose_name=lazy("subscribed to newsletter")
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=lazy("profile created at")
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name=lazy("profile updated at")
    )

    class Meta:
        verbose_name = lazy("reader profile")
        verbose_name_plural = lazy("reader profiles")

    def __str__(self):
        return f"Reader Profile of {self.user.email}"

    def subscribe_newsletter(self):
        self.subscribed_newsletter = True
        self.save(update_fields=["subscribed_newsletter"])

    def unsubscribe_newsletter(self):
        self.subscribed_newsletter = False
        self.save(update_fields=["subscribed_newsletter"])
