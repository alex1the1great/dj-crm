from django.test import SimpleTestCase
from django.urls import reverse


class LandingPageTests(SimpleTestCase):

    def test_landing_page_template(self):
        response = self.client.get(reverse('pages:landing_page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/landing.html')
        self.assertContains(response, 'CRM builds with Django')
        self.assertNotContains(response, 'This content is not available')
