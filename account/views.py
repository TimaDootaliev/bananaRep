# обработчики запросов
from rest_framework.views import APIView

from .serializers import (RegistrationSerializer)


class RegistrationView(APIView):
    def post(self, request):
        serializer = RegistrationSerializer(request.data)
        if serializer.is_valid():
            pass

class ActivationView(APIView):
    pass


class LoginView(APIView):
    pass


class LogoutView(APIView):
    pass


class ForgotPasswordView(APIView):
    pass


class ChangePasswordView(APIView):
    pass

