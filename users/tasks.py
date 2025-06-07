from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail


@shared_task
def send_verification_code(email, code):
    send_mail(
        subject='Подтверждение регистрации',
        message=f'Ваш код для регистрации на портале: {code}',
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[email]
    )