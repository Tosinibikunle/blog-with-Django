from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'posts', views.PostListAPIView, basename='post')

urlpatterns = [
    path('/', views.PostListView.as_view(), name='post_list'),
    path('/<int:post_id>/', views.PostDetailView.as_view(), name='post_detail'),
    path('/author/<int:author_id>/', views.PostAuthorView.as_view(), name='author_posts'),
    path('/author/name/<str:author_name>/', views.PostAuthorView.as_view(), name='author_name_posts'),
    path('/author/email/<str:author_email>/', views.PostAuthorView.as_view(), name='author_email_posts'),
]