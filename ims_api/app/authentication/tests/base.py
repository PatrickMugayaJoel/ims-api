from rest_framework.test import APIClient, APITestCase
from django.urls import reverse
from .company_test_data import valid_company_data1


class BaseTestCase(APITestCase):
    def setUp(self):
        self.assertEqual(21, 21)
        self.client = APIClient()
        self.company_url = reverse("authentication:register_company")
        company_res = self.client.post(self.company_url, valid_company_data1, format='json')
        self.company_id = company_res.data['id']
