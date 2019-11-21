
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.hashers import make_password

from ims_api.app.utilities import remove_fields
from ims_api.app.constants import excluded_fields

from .serializers import LoginSerializer, SignUpCompanySerializer,\
                         CreateUserSerializer
from .validators import check_request_body
from .models import Company


class SignUpCompanyAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = SignUpCompanySerializer

    def post(self, request):
        company = request.data.get('company', {})
        check_request = check_request_body(company, 'company')
        if check_request:
            return Response({'error': check_request['error']}, status=400)
        if not company['profile_pic']:
            company['profile_pic'] = 'https://i.imgur.com/Fg1dopm.png'
        serializer = self.serializer_class(data=company)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['password'] = make_password(company["password"])
        serializer.save()
        response_data = serializer.data
        remove_fields(excluded_fields, response_data)
        return Response(response_data, status=status.HTTP_201_CREATED)


class UserView(APIView):
    serializer_class = CreateUserSerializer
    
    def post(self, request, pk):
        user = request.data.get('user', {})
        check_request = check_request_body(user, 'user')
        if check_request:
            return Response({'error': check_request['error']}, status=400)
        try:
            user_company = Company.objects.get(id=pk)
        except:
            return Response({'error': 'Company doesnot exist'}, status=400)
        user['user_company'] = user_company.id
        if not user['profile_pic']:
            user['profile_pic'] = 'https://imgur.com/a/zfb51g5'
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['password'] = make_password(user['password'])
        serializer.save()
        response_data = serializer.data
        remove_fields(excluded_fields, response_data)
        return Response(response_data, status=status.HTTP_201_CREATED)
        
        
class LoginAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request):
        user = request.data.get('user', {})
        
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
