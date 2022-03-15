from register.models import RegisterLogin
from django.db.models import Q
from django.contrib.auth.backends import BaseBackend


class CustomAuthenticationBackend(BaseBackend):
    def get_user(self, user_id):
        try:
            return RegisterLogin.objects.get(pk=user_id)
        except RegisterLogin.DoesNotExist:
            return None

    def authenticate(self, request, username=None, password=None):
        try:
            user = RegisterLogin.objects.get(
                Q(username=username) | Q(patient_id=username)
            )
        except RegisterLogin.DoesNotExist:
            return None
        return user if user.check_password(password) else None
