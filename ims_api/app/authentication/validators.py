from django.core.exceptions import ValidationError
from .models import Company, User
import re

def validate_company_name(company_name):
    check_company_name = Company.objects.filter(company_name=company_name)
    if check_company_name.exists():
        raise ValidationError(f"company name '{company_name}' is already taken")
    
def validate_email(email):
    check_company_email = Company.objects.filter(email=email)
    check_user_email = User.objects.filter(email=email)
    error_message = f"this email '{email}' is already taken"
    if check_company_email.exists():
        raise ValidationError(error_message)
    elif check_user_email.exists():
        raise ValidationError(error_message)
    
def validate_password(password):
    """
        validates that  password is longer than 8 characters
        password is alphanumeric
    """
    if len(password) < 8:
        raise ValidationError(
            "Password should atleast be 8 characters.")
    if not re.search(r'[0-9]', password) or not re.search(r'[a-zA-Z]', password) or not re.search(r'[!?@#$%^&*.]', password):
        raise ValidationError(
            "Password should include numbers and alphabets and one special character")
    if re.search(r'[\s]', password):
        raise ValidationError(
            "Password should not include white spaces")

def check_request_body(request_data, request_type):
    """
    Validates request to ensure that required fields are included
    """
    company_keys = ['company_name', 'email', 'password', 'profile_pic']
    user_keys = ['first_name', 'last_name', 'email', 'password', 'profile_pic']
    if request_type == 'company':
        required_keys = company_keys
    else:
        required_keys = user_keys
    for key in required_keys:
        if key not in request_data.keys():
            return {'error': f'{key} field is missing'}
    return None
