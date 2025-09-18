from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'likes', views.LikeViewSet, basename='like')

urlpatterns = [
    path('unlike/<int:pk>/', views.LikeDeleteView.as_view(), name='like-delete'),
    path('likes/<int:post_id>/', views.LikeListViewSet.as_view(), name='like-list'),
    path('likes/count/<int:post_id>/', views.LikeCountView.as_view(), name='like-count'),
    path('', include(router.urls)),  # include router-generated routes
]
