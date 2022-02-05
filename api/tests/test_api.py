from rest_framework import status
from rest_framework.test import APIRequestFactory, RequestsClient
from django.urls import include, path, reverse
from rest_framework.test import APITestCase, URLPatternsTestCase, APIClient

factory = APIRequestFactory(enforce_csrf_checks=True)
client = APIClient(enforce_csrf_checks=True)
client_response = RequestsClient()
client.get('/api/blog', content_type='application/json')
request = factory.get('/api/blog', content_type='application/json')


class BlogTests(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        path('api/', include('api.urls'))
    ]

    def test_create_blog(self):
        url = reverse('blog')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
