from rest_framework.decorators import *
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import *
from .serializers import UsersRegistrationSerializer


class RegistrationView(APIView):
    permission_classes(AllowAny, )
    serializer_class = UsersRegistrationSerializer

    def post(self, request):

        if request.method == 'POST':
            serializer = UsersRegistrationSerializer(data=request.data)
            data = {}

            if serializer.is_valid():
                user = serializer.save()
                data['response'] = 'Welcome,' '%s' % user.surname
            else:
                data = serializer.errors
            return Response(data)




