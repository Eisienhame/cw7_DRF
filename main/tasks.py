from config import settings
from config.celery import app
from main.models import Habit
from celery import shared_task


import telebot


@app.task
def send_tg_create_message(habit_id):
    """Отправка сообщения через бот TG"""
    bot = telebot.TeleBot(settings.TG_BOT_TOKEN)
    message = f"Создание привычки {habit.name}"
    bot.send_message(habit.owner.chat_id, message)

@shared_task
def check_habit():
    token = settings.TG_HABBIT_BOT_TOKEN
    bot = telebot.TeleBot(token)
    now = datetime.now().time()  # Текущее время
    users = User.objects.filter(tg_chat_id__isnull=False)

    for user in users:

        # Получить все записи привычек, где поле 'время' меньше или равно текущему времени
        habits_to_complete = Habit.objects.filter(time__lte=now, user=user)

        for habit in habits_to_complete:
            habit_time = habit.time

            # Получить периодичность привычки
            frequency = habit.periodic
            # Определить интервал в зависимости от периодичности
            if frequency == '1':
                interval = timedelta(days=1)
            elif frequency == '2':
                interval = timedelta(days=2)
            elif frequency == '3':
                interval = timedelta(days=3)
            else:
                continue

            current_time = datetime.combine(datetime.today(), now)
            habit_datetime = datetime.combine(datetime.today(), habit_time)

            # Разница между текущим временем и временем привычки
            time_difference = current_time - habit_datetime

            # Проверить, наступило ли время выполнения привычки с учетом переодичности
            if time_difference.total_seconds() >= 0 and time_difference.total_seconds() % interval.total_seconds() == 0:
                message = f"Пора выполнить привычку: {habit.name}"
                bot.send_message(user.tg_chat_id, message)