from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from apps.analytics.models import PageView, ClickEvent
from apps.analytics.serializers import PageViewSerializer, ClickEventSerializer

User = get_user_model()

class AnalyticsAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser',    
            password='testpass'
        )
        self.client.force_authenticate(user=self.user)
        self.page_view = PageView.objects.create(
            user=self.user,
            page_url='http://example.com/page1',
            session_id='session123',
            referrer_url='http://referrer.com',
        )
        self.click_event = ClickEvent.objects.create(
            user=self.user,
            element_id='button1',
            page_url='http://example.com/page1',
            session_id='session123',
            referrer_url='http://referrer.com',
        )

class PageViewAPITests(AnalyticsAPITestCase):
    def test_list_page_views(self):
        url = reverse('page-view-list')
        response = self.client.get(url)
        page_views = PageView.objects.all()
        serializer = PageViewSerializer(page_views, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_retrieve_page_view(self):
        url = reverse('page-view-detail', args=[self.page_view.id])
        response = self.client.get(url)
        serializer = PageViewSerializer(self.page_view)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data) 
