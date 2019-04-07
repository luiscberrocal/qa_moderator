from django.urls import reverse
from test_plus import TestCase


class TestAppInfo(TestCase):

    def test_version(self):
        url = reverse('core-api:app-info')
        #client = APIClient()
        response = self.client.get(url)
        version_data = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertRegex(version_data.get('version'), r'\d+\.\d+\.\d+')
