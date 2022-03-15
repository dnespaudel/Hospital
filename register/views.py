from django.core.exceptions import ObjectDoesNotExist
from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from register.serializers import *
from register.backend import CustomAuthenticationBackend
from register.permissions import *
from rest_condition import And, Or
from rest_framework.response import Response
from rest_framework import status
import pyotp
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail.message import EmailMultiAlternatives


User = get_user_model()


class generateKey:
    @staticmethod
    def returnValue():
        secret = pyotp.random_base32()
        totp = pyotp.TOTP(secret, interval=180)
        OTP = totp.now()
        return {"totp": secret, "OTP": OTP}


class RegisterView(APIView):
    @csrf_exempt
    def post(self, request):
        serialized = RegisterSerializer(data=request.data)
        if serialized.is_valid():
            key = generateKey.returnValue()
            user = User(
                first_name=serialized.data['first_name'],
                last_name=serialized.data['last_name'],
                phone_number=serialized.data['phone_number'],
                email=serialized.data['email'],
                username=serialized.data['username'],
                address=serialized.data['address'],
                mfa_hash=key['totp'],
                otp=key['OTP'],
            )
            try:
                validate_password(serialized.data['password'], user)
            except ValidationError as e:
                return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
            user.set_password(serialized.data['password'])
            user.role = "P"
            user.is_verified = False
            user.save()
            email_template = render_to_string('otp_send.html',
                                              {"otp": key['OTP'], "first_name": serialized.data['first_name']})
            sign_up = EmailMultiAlternatives(
                "Otp Verification",
                "Otp Verification",
                settings.EMAIL_HOST_USER,
                [serialized.data['email']],
            )
            sign_up.attach_alternative(email_template, 'text/html')
            sign_up.send()

            return Response(serialized.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)


class ReSendOtp(APIView):
    @csrf_exempt
    def get_object(self, pk):
        try:
            return RegisterLogin.objects.get(pk=self.kwargs.get('pk'))
        except RegisterLogin.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @csrf_exempt
    def post(self, request, pk):
        response = {}
        user = self.get_object(pk)
        try:
            if user.is_verified:
                return Response(
                    {'msg': 'User is already verified'}, status=status.HTTP_200_OK
                )
            try:
                key = generateKey.returnValue()
                user.mfa_hash = key['totp']
                user.otp = key['OTP']
                email_template = render_to_string('otp_send.html',
                                                  {"otp": key['OTP'], "full_name": user.first_name})
                sign_up = EmailMultiAlternatives(
                    "ReSent Otp Verification",
                    "ReSent Otp Verification",
                    settings.EMAIL_HOST_USER,
                    [user.email],
                )
                sign_up.attach_alternative(email_template, 'text/html')
                sign_up.send()

                user.save()
                response['data'] = user.data
                return Response(user, status=status.HTTP_201_CREATED)
            except:
                return Response(
                    {"msg": "New OTP has been sent to your email, Please use it for verification"},
                    status=status.HTTP_400_BAD_REQUEST
                )
        except:
            if ObjectDoesNotExist:
                return Response({'msg': 'No User found!'}, status=status.HTTP_400_BAD_REQUEST)


class VerifyOTP(APIView):

    def post(self, request, otp):
        try:
            user = RegisterLogin.objects.get(otp=otp, is_verified=False)
            if otp != user.otp:
                return Response({"Otp": "Invalid otp"}, status=status.HTTP_406_NOT_ACCEPTABLE)
            else:
                mfa_hash = user.mfa_hash
                totp = pyotp.TOTP(mfa_hash, interval=180)
                verify = totp.verify(otp)

                if verify:
                    user.is_verified = True
                    user.save()
                    email_template = render_to_string('register_success.html', {"full_name": user.first_name})
                    sign_up = EmailMultiAlternatives(
                        "Account successfully activated",
                        "Account successfully activated",
                        settings.EMAIL_HOST_USER,
                        [user.email],
                    )
                    sign_up.attach_alternative(email_template, 'text/html')
                    sign_up.send()

                    return Response({"Verify success": "Your account has been successfully activated!!"},
                                    status=status.HTTP_202_ACCEPTED)
                else:
                    return Response({"Time out": "Given otp is expired!!"}, status=status.HTTP_408_REQUEST_TIMEOUT)

        except:
            return Response({"No User": "Invalid otp OR no active user found for the given otp"},
                            status=status.HTTP_400_BAD_REQUEST)


class RegisterListView(generics.ListAPIView):
    # permission_classes = [And(IsAuthenticated), Or(isAdmin, IsAdminUser, isManager)]
    queryset = RegisterLogin.objects.all()
    serializer_class = RegisterSerializer


class RegisterDetailView(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [And(IsAuthenticated), Or(isAdmin, IsAdminUser, isPatient, isDoctor, isNurse, isReceptionist,
    #                                                isManager)]
    queryset = RegisterLogin.objects.all()
    serializer_class = RegisterDetailSerializer


class LoginView(TokenObtainPairView):
    queryset = ''
    serializer_class = LoginSerializer

    def perform_authentication(self, request):
        return CustomAuthenticationBackend()


class RolesUpdateView(generics.UpdateAPIView):
    queryset = ''
    permission_classes = [And(IsAuthenticated), Or(isAdmin, IsAdminUser, isManager)]
    serializer_class = RolesSerializer

    def get_object(self):
        try:
            self.user = RegisterLogin.objects.get(pk=self.kwargs.get('pk'))
        except RegisterLogin.DoesNotExist:
            raise ValidationError(
                {'error': 'User does not exist.'}
            )
        return self.user

    def perform_update(self, serializer):
        data = serializer.validated_data
        for key in data.keys():
            setattr(self.user, key, data.get(key))
        self.user.save()
