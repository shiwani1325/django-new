from django.conf import settings
from django.core.mail import send_mass_mail

def send_account_activation_email(email,email_token):
    subject="your account need to be verified"

    email_from=settings.EMAIL_HOST_USER
    message=f'Hi, click on the link to activate your account http://127.0.0.1:8000/accounts/activate/{email_token}'
    send_mass_mail(subject,message,email_from,[email])

