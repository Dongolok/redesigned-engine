from django.urls import path, include
from .apiviews import RegistrationAPIView, LoginAPIView


urlpatterns = [

    path('register/', RegistrationAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),


]
