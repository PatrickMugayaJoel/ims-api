from django.urls import path
from .views import CreateItenary


urlpatterns = [
    path('company/<int:pk>/itenaries/',
         CreateItenary.as_view(), name="create_itenary")
         ]
