from django.urls import path
from .views import CommentListCreateView, CommentDeleteView, CommentDetailView

urlpatterns = [
    path("/", CommentListCreateView.as_view(), name="comment-list-create"),
    path("<int:pk>/", CommentDetailView.as_view(), name="comment-detail"),
    path(
        "<int:pk>/delete/", CommentDeleteView.as_view(), name="comment-delete"
    ),
]
