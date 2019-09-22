from django.urls import path

from ims_api.app.authentication.views import LoginAPIView, SignUpCompanyAPIView, UserView

urlpatterns = [
    path('users/login/', LoginAPIView.as_view()),
    path('companies/', SignUpCompanyAPIView.as_view(), name="register_company"),
    path('companies/<int:pk>/users/', UserView.as_view(), name="create_user"),
]
