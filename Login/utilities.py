from project import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def send_activation_email(to_email_id, token):
    subject = "Activation mail"
    html_message = html_message = render_to_string('Login/mail_template.html', {'context': token})
    plain_message = strip_tags(html_message)
    from_email = settings.EMAIL_HOST_USER
    to = to_email_id
    send_mail(subject, plain_message, from_email, [to], html_message = html_message,fail_silently=True)

