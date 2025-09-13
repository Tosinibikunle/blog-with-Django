from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewset, TagViewset

router = DefaultRouter()
router.register(r"categories", CategoryViewset)
router.register(r"tags", TagViewset)

urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls")),
]
