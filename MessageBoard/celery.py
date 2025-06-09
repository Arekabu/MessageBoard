import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MessageBoard.settings')

app = Celery('MessageBoard')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'every_monday_8am_notification': {
        'task': 'post.tasks.weekly_notification',
        'schedule': crontab(hour=8, minute=0, day_of_week=1),
    },
}
