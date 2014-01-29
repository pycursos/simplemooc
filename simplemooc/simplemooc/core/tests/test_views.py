from django.test import TestCase, Client
from django.core.urlresolvers import reverse


class HomeTestCase(TestCase):

    def test_template_home_view(self):
        home_url = reverse('core:home')
        client = Client()
        response = client.get(home_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('home.html')