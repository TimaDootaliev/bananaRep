from django.contrib.auth import get_user_model
from rest_framework import serializers


User = get_user_model()


class RegistrationSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(min_length=6, required=True)
    password_confirm = serializers.CharField(min_length=6, required=True)
    name = serializers.CharField(max_length=50, required=True)
    last_name = serializers.CharField(required=False)

    def validate_email(self, email):
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError('Адрес уже зарегистрирован')
        return email





class ActivationSerializer(serializers.Serializer):
    pass


class LoginSerializer(serializers.Serializer):
    pass


class ChangePasswordSerializer(serializers.Serializer):
    pass


class ForgotPasswordSerializer(serializers.Serializer):
    pass
