import telebot
from config import BOT_TOKEN, OWNER_ID
from commands import (
    admin_commands,
    settings_commands,
    lock_commands,
    fun_commands,
    dev_commands,
    service_commands
)

bot = telebot.TeleBot(BOT_TOKEN)

all_commands = (
    admin_commands +
    settings_commands +
    lock_commands +
    fun_commands +
    dev_commands +
    service_commands
)

@bot.message_handler(commands=['start'])
def start(message):
    if message.from_user.id == OWNER_ID:
        bot.reply_to(message, "👑 أهلاً بك مالك SimoGuard\nالبوت يعمل.")
    else:
        bot.reply_to(message, "🛡️ SimoGuard يعمل لحماية المجموعات.")

@bot.message_handler(func=lambda message: True)
def commands(message):
    text = message.text

    if text in all_commands:
        bot.reply_to(
            message,
            f"✅ الأمر موجود:\n{text}\n\nسيتم تفعيل وظيفته قريباً."
        )

bot.infinity_polling()
