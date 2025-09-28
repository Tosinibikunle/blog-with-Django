from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'posts', views.PostViewSet)

urlpatterns = [
    path('posts/', views.PostListView.as_view(), name='post_list'),
    path('posts/<int:post_id>/', views.PostDetailView.as_view(), name='post_detail'),
    path('posts/author/<int:author_id>/', views.PostAuthorView.as_view(), name='author_posts'),
    path('posts/author/name/<str:author_name>/', views.PostAuthorView.as_view(), name='author_name_posts'),
    path('posts/author/email/<str:author_email>/', views.PostAuthorView.as_view(), name='author_email_posts'),
]