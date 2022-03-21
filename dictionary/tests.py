from urllib import response
from django.test import SimpleTestCase


class URRTests(SimpleTestCase):
    def test_get_index_url(self):
        """
            Test to successfully get the index page/url
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_get_invalid_url(self):
        response = self.client.get('/word')
        self.assertEqual(response.status_code, 404)