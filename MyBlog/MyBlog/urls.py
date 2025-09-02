from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),

    # Example app routes
    path("accounts/", include("apps.accounts.urls")),
    path("posts/", include("apps.posts.urls")),
    path("comments/", include("apps.comments.urls")),
    path("likes/", include("apps.likes.urls")),
    path("categories/", include("apps.categories.urls")),
    path("analytics/", include("apps.analytics.urls")),
]
