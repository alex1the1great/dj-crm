from django.test import SimpleTestCase
from django.urls import reverse


class LandingPageTests(SimpleTestCase):

    def test_landing_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_landing_page_url_name(self):
        response = self.client.get(reverse('pages:landing_page'))
        self.assertEqual(response.status_code, 200)
