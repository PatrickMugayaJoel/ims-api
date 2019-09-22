from django.urls import path

from .views import LoginAPIView, SignUpCompanyAPIView

urlpatterns = [
    path('users/login/', LoginAPIView.as_view()),
    path('users/', SignUpCompanyAPIView.as_view()),
]
