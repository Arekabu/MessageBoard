from django.apps import AppConfig
import redis
import os
from dotenv import load_dotenv


load_dotenv()

class PostConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'post'

    def ready(self):
        import post.signals

# red = redis.Redis(
#     host=os.getenv('REDIS_ENDPOINT'),
#     port=os.getenv('REDIS_PORT'),
#     password=os.getenv('REDIS_PASSWORD')
# )
