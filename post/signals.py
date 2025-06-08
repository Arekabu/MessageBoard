from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Comment
from .tasks import new_comment_notification, approved_comment_notification


@receiver(post_save, sender=Comment)
def notify_about_new_comment(sender, instance, created, **kwargs):
    if created:
        new_comment_notification.apply_async([instance.pk])


@receiver(post_save, sender=Comment)
def notify_about_new_comment(sender, instance, created, **kwargs):
    if (not created and
            kwargs.get('update_fields') and
            'approved' in kwargs['update_fields'] and
            instance.approved):
        approved_comment_notification.apply_async([instance.pk])
