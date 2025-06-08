from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from .models import Post, Comment


@shared_task
def new_comment_notification(comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if not comment:
        return

    post = comment.post

    if post.author == comment.user:
        return

    author = post.author
    profile_url = f"{settings.SITE_URL}/users/{author.pk}"

    html_message = render_to_string(
        'emails/new_comment.html',
        {
            'post': post,
            'profile_url': profile_url,
            'comment_author': comment.user.username,
        }
    )

    text_message = f"""
    У вас новый комментарий к объявлению "{post.title}".
    Проверьте его на странице профиля: {profile_url}
    """

    send_mail(
        subject=f'Новый комментарий к объявлению "{post.title}"',
        message=text_message,
        html_message=html_message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[author.email]
    )


@shared_task
def approved_comment_notification(comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if not comment:
        return

    post = comment.post

    if post.author == comment.user:
        return

    email = comment.user.email
    post_url = f"{settings.SITE_URL}/posts/{post.pk}"

    html_message = render_to_string(
        'emails/approved_comment.html',
        {
            'post': post,
            'post_url': post_url,
        }
    )

    text_message = f"""
        Пользователь {post.author} одобрил ваш комментарий к объявлению "{post.title}".
        Перейти к объявлению: {post_url}
        """

    send_mail(
        subject=f'Ваш комментарий к объявлению "{post.title}" одобрен.',
        message=text_message,
        html_message=html_message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[email]
    )
