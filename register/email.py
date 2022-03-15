from templated_mail.mail import BaseEmailMessage


class SendEmail(BaseEmailMessage):
    template_name = 'otp_send.html'