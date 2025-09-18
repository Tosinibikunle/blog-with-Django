from django.urls import path
# from django.utils.translation import gettext_lazy as lazy
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'likes', views.LikeViewSet, basename='like')

urlpatterns = [
    path('like/', views.LikeCreateViewSet.as_view(), name='like-create'),
    path('unlike/', views.LikeDeleteView.as_view(), name='like-delete'),
    path('likes/<int:post_id>/', views.LikeListView.as_view(), name='like-list'),
    path('likes/count/<int:post_id>/', views.LikeCountView.as_view(), name='like-count'),
]

urlpatterns += router.urls
