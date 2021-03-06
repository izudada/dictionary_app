from urllib import response
from django.test import Client, SimpleTestCase, TestCase
from django.urls import resolve, reverse

from .views import index


class TestURLs(SimpleTestCase):
    def test_get_index_url(self):
        """
            Test to successfully get the index page/url
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_get_invalid_url(self):
        response = self.client.get('/word')
        self.assertEqual(response.status_code, 404)

    def test_index_url_is_resolved(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func, index)


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.index_url = reverse('index')
    
    def test_index_GET(self):
        response = self.client.get(self.index_url)
        self.assertAlmostEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')