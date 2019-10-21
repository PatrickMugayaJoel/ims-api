from django.core.exceptions import ValidationError
from .models import Company

def validate_company_name(company_name):
    check_company_name = Company.objects.filter(company_name=company_name)
    if check_company_name.exists():
        raise ValidationError("Company Name already exists")
    