
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import LoginSerializer, SignUpCompanySerializer

from .models import Company

class SignUpCompanyAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = SignUpCompanySerializer

    def post(self, request):
        # print(request.data)
        company = request.data.get('company', {})
        serializer = self.serializer_class(data=company)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        print("*********yes*****", serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)

class LoginAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request):
        user = request.data.get('user', {})
        
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
