from django.urls import reverse
from rest_framework.test import APIClient, APITestCase

class BaseTestCase(APITestCase):
    """ 
    Base Test class for out tests in this app
    Class will also house the setup
    method for our test
    """

    def setUp(self):
        # Initialize the Testclient for the test
        self.client = APIClient()

    def test_welcome_endpoint(self):
        url = reverse('welcome')
        response = self.client.get(url)
        self.assertEqual(response.data['Index'], 'Welcome to ims-api')

