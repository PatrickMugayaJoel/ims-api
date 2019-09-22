from .base import BaseTestCase
from .company_test_data import *


class CompanyTestCase(BaseTestCase):
    def test_signup_company_succeeds(self):
        res = self.client.post(self.company_url, valid_company_data, format='json')
        self.assertEqual(res.status_code, 201)
        self.assertEqual(res.data["company_name"], 'isabirye and sons')
        self.assertIsInstance(res.data, dict)

    def test_signup_company_failure_if_a_field_is_missing(self):
        res = self.client.post(self.company_url, company_missing_field, format='json')
        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.data['error'], 'profile_pic field is missing')

    def test_signup_company_failure_if_a_field_is_blank(self):
        res = self.client.post(self.company_url, company_blank_field, format='json')
        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.data['email'][0], 'email field can not be blank')
        
    def test_signup_company_failure_if_email_is_invalid(self):
        res = self.client.post(self.company_url, company_invalid_email, format='json')
        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.data['email'][0], 'Enter a valid email address.')
        
    def test_signup_company_failure_if_company_name_is_short(self):
        res = self.client.post(self.company_url, company_short_name, format='json')
        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.data['company_name'][0], 'company name must be atleast 3 characters')
        
    def test_signup_company_failure_if_company_password_is_short(self):
        res = self.client.post(self.company_url, company_short_password, format='json')
        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.data['password'][0], 'Password should atleast be 8 characters.')
