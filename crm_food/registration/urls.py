from django.urls import path, include
from .apiviews import RegistrationCreateView, RegistrationListView, LoginAPIView


urlpatterns = [

    # path('register/', RegistrationAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
    path('registration/', RegistrationCreateView.as_view()),
    path('users/', RegistrationListView.as_view())



]
