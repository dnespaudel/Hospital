from django.urls import path
from register.views import *
from rest_framework_simplejwt import views as jwt_views

app_name = "register"

urlpatterns = [
    path('register', RegisterView.as_view()),
    path('register/all', RegisterListView.as_view()),
    path('register/<pk>', RegisterDetailView.as_view()),
    path('roles/<pk>', RolesUpdateView.as_view()),
    path('verify/<int:otp>', VerifyOTP.as_view()),
    path('resend/otp/<pk>', ReSendOtp.as_view()),
    path('login', LoginView.as_view()),
    path('login/refresh', jwt_views.TokenRefreshView.as_view(), name='Token Refresh'),
]