from config import settings
from config.celery import app
from main.models import Habit

import telebot



@app.task
def send_telegram_message(habit_id):
    """Отправка сообщения через бот TG"""
    habit = Habit.objects.get(id=habit_id)
    bot = telebot.TeleBot(settings.TG_BOT_TOKEN)
    message = f"Напоминание о выполнении привычки {habit.name}"
    bot.send_message(habit.owner.chat_id, message)

