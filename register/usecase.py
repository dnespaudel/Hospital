# from register.email import SendEmail
# from register.models import *
#
#
# class OtpSendUseCase:
#     def __init__(self, serializer):
#         self.serializer = serializer
#         self.data = serializer.validated_data
#
#     def execute(self):
#         self._factory()
#
#     def _factory(self):
#         self._otp = RegisterLogin(**self.data)
#         self._otp.save()
#
#         SendEmail(
#             context={
#                 'email': self._otp.email,
#                 'otp': self._otp.otp,
#             }
#         ).send(to=[self._otp.email])