from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as lazy
# from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class PageView(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, related_name='page_views')
    page_url = models.URLField(verbose_name=lazy("page URL"))
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name=lazy("viewed at"))
    session_id = models.CharField(max_length=255, null=True, blank=True, verbose_name=lazy("session ID"))
    referrer_url = models.URLField(null=True, blank=True, verbose_name=lazy("referrer URL"))
    user_agent = models.CharField(max_length=512, null=True, blank=True, verbose_name=lazy("user agent"))
    ip_address = models.GenericIPAddressField(null=True, blank=True, verbose_name=lazy("IP address"))

    class Meta:
        verbose_name = lazy("page view")
        verbose_name_plural = lazy("page views")
        ordering = ['-timestamp']

    def __str__(self):
        return f"PageView: {self.page_url} at {self.timestamp}"

    def get_user_info(self):
        return {
            "user_id": self.user.id if self.user else None,
            "email": self.user.email if self.user else None,
            "username": self.user.username if self.user else None,
        }
class ClickEvent(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, related_name='click_events')
    element_id = models.CharField(max_length=255, verbose_name=lazy("element ID"))
    page_url = models.URLField(verbose_name=lazy("page URL"))
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name=lazy("clicked at"))
    session_id = models.CharField(max_length=255, null=True, blank=True, verbose_name=lazy("session ID"))
    referrer_url = models.URLField(null=True, blank=True, verbose_name=lazy("referrer URL"))
    user_agent = models.CharField(max_length=512, null=True, blank=True, verbose_name=lazy("user agent"))
    ip_address = models.GenericIPAddressField(null=True, blank=True, verbose_name=lazy("IP address"))

    class Meta:
        verbose_name = lazy("click event")
        verbose_name_plural = lazy("click events")
        ordering = ['-timestamp']

    def __str__(self):
        return f"ClickEvent: {self.element_id} on {self.page_url} at {self.timestamp}"

    def get_user_info(self):
        return {
            "user_id": self.user.id if self.user else None,
            "email": self.user.email if self.user else None,
            "username": self.user.username if self.user else None,
        }    