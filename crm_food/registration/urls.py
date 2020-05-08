from django.urls import path, include
from .apiviews import RegistrationView


urlpatterns = [

    # path('register/', RegistrationAPIView.as_view()),
    # path('login/', LoginAPIView.as_view()),
    path('registration/', RegistrationView.as_view()),



]
