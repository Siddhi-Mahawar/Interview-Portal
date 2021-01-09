from project import settings
from django.core.mail import send_mail

def send_activation_email(to_email_id, token):
    subject = "Activation mail"
    message = token
    from_list = settings.EMAIL_HOST_USER
    to_list = to_email_id
    send_mail(subject, message, from_list, to_list, fail_silently=True)

