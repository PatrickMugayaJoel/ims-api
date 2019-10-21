from rest_framework.generics import CreateAPIView
from ims_api.app.itenaries.models import Itenary
from rest_framework.response import Response
from rest_framework import status
from .serializers import ItenarySerializer
from .validators import validate_create_itenary_request,\
    assign_thumbnail_value, check_if_itenary_exists, check_if_company_exists


class CreateItenary(CreateAPIView):
    """
    View class for creating an itenary
    """
    serializer_class = ItenarySerializer

    def create(self, request, pk):
        """
        Method creates a new itenay

        args:
            request - maps to the request object
            pk      - maps to the id of the company an itenary is created for
        """
        request_data = request.data
        validate_request = validate_create_itenary_request(request_data)
        if validate_request['error'] != 'None':
            return Response({'error': validate_request['error']}, status=400)
        thumbnail = assign_thumbnail_value(request_data)
        name = request_data['name']
        company = check_if_company_exists(pk)
        if not company:
            return Response({'error': 'Company doesnot exist'}, status=400)
        data = {
            'name': name,
            'thumbnail': thumbnail
        }
        check_itenary = check_if_itenary_exists(name, pk)
        if check_itenary != 'None':
            return Response({'error': check_itenary['error']}, status=400)
        serializer = ItenarySerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response_data = serializer.data
        response_data.pop('company_id')
        return Response({'itenary': response_data}, status=201)
