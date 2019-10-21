from django.core.exceptions import ValidationError
from rest_framework.response import Response
from ims_api.app.authentication.models import Company
from .models import Itenary

def validate_create_itenary_request(request):
    """
    Validates request to ensure that required fields are included
    """
    required_keys = ['name', 'thumbnail']
    for key in required_keys:
        if key not in request.keys():
            return {'error': f'{key} field is required'}
    return {'error': 'None'}

def assign_thumbnail_value(request):
    """
    Assigns a default thumbnail value if no value is given
    """
    if not request['thumbnail']:
        return "No thumnail"
    else:
        return request['thumbnail']

def check_if_itenary_exists(itenary_name, company_id):
    """
    Checks if an itenary already exists.
    This is done by querying the Itenary object using the given name an company id.
    """
    fetch_itenary = Itenary.objects.filter(name=itenary_name, company_id=company_id)
    if fetch_itenary.exists():
        return {'error': 'Itenary already exists'}
    return 'None'

def check_if_company_exists(company_id):
    """
    Checks if the company a user is creating the itenary for exists
    """
    try:
        return Company.objects.get(id=company_id)
    except:
        return None
