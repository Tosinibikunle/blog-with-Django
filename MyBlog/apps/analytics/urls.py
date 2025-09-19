from django.urls import path
from . import views


urlpatterns = [
    path('page-views/', views.PageViewList.as_view(), name='page-view-list'),
    path('click-events/', views.ClickEventList.as_view(), name='click-event-list'),
    path('page-views/<int:pk>/', views.PageViewDetail.as_view(), name='page-view-detail'),
    path('click-events/<int:pk>/', views.ClickEventDetail.as_view(), name='click-event-detail'),]