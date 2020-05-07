from django.urls import path, include
from .apiviews import RegistrationView
from rest_framework_simplejwt.views import (
    TokenObtainSlidingView,
    TokenRefreshSlidingView,
)


urlpatterns = [
    # path('', include('djoser.urls')),
    # path('', include('djoser.urls.authtoken')),
    path('register/', RegistrationView.as_view()),
    path('api/token/', TokenObtainSlidingView.as_view(), name='token_obtain'),
    path('api/token/refresh/', TokenRefreshSlidingView.as_view(), name='token_refresh'),

]
