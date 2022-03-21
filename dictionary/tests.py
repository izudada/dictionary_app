from django.test import TestCase


class URRTests(TestCase):
    def test_get_index_url(self):
        """
            Test to successfully get the index page/url
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)