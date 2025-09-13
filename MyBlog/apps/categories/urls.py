from django.urls import path, include
from .views import CategoryViewset, TagViewset
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r"categories", CategoryViewset)
router.register(r"tags", TagViewset)

urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls")),
    path("api/", include(router.urls)),
    path("api/categories/", include("categories.urls")),
    path("api/tags/", include("tags.urls")),
]
