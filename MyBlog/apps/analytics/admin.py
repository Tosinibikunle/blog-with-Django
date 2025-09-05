from django.contrib import admin
from .models import PageView, ClickEvent


# Register your models here.
admin.site.register(PageView)
admin.site.register(ClickEvent)
