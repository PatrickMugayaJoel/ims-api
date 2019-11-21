from .base import BaseTestCase
from .company_test_data import valid_user_data


class UserTestCase(BaseTestCase):

    def test_add_user_to_company_succeeds(self):
        user_url = f"/api/companies/{self.company_id}/users/"
        res = self.client.post(user_url, valid_user_data, format='json')
        self.assertEqual(res.status_code, 201)
        self.assertEqual(res.data['first_name'], 'kenneth')
        self.assertEqual(res.data['last_name'], 'sanya')
