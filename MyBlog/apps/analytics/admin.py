from django.contrib import admin
from .models import PageView, ClickEvent


admin.site.register(PageView)
admin.site.register(ClickEvent)
