from django.urls import path
from . import views

urlpatterns = [
    # Existing routes
    path("", views.article_list, name="list"),
    path("<slug:slug>", views.article_detail, name="detail"),
    # Placeholder routes
    path("create/", views.article_create, name="create"),
    path("<slug:slug>/edit/", views.article_edit, name="edit"),
    path("<slug:slug>/delete/", views.article_delete, name="delete"),
    path("category/<str:category>/", views.article_by_category, name="by_category"),
    path("search/", views.article_search, name="search"),
    path("archive/<int:year>/<int:month>/", views.article_archive, name="archive"),
]
