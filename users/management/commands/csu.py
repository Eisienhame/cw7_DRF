from django.core.management import BaseCommand
from users.models import User
import os
from config.settings import TG_CHAT_ID


class Command(BaseCommand):

    def handle(self, *args, **options):

        user = User.objects.create(
            email='admin@yandex.ru',
            tg_chat_id=TG_CHAT_ID,
            is_staff=True,
            is_superuser=True

        )

        user.set_password(f'{os.getenv("bd_pass")}')
        user.save()
