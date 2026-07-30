import telebot
from config import BOT_TOKEN, OWNER_ID
from modules.ranks import setup_ranks
from modules.admin import setup_admin
bot = telebot.TeleBot(BOT_TOKEN)
setup_ranks(bot)
setup_admin(bot)
from permissions import can_kick, can_manage
print("SimoGuard Started...")


@bot.message_handler(commands=['start'])
def start(message):
    if message.from_user.id == OWNER_ID:
        bot.reply_to(
            message,
            "👑 أهلاً بك مالك SimoGuard\n"
            "🛡️ البوت يعمل."
        )
    else:
        bot.reply_to(
            message,
            "🛡️ SimoGuard يعمل."
        )


@bot.message_handler(commands=['help'])
def help_command(message):
    bot.reply_to(
        message,
        """
🛡️ أوامر SimoGuard

👮 الإدارة:
- حظر / ban
- كتم / mute
- طرد / kick

⚙️ الخدمات:
- الاوامر /help
- ايدي /id

استخدم الأوامر بالرد على رسالة العضو.
        """
    )


@bot.message_handler(func=lambda m: m.text in ["الاوامر", "help"])
def commands(message):
    bot.reply_to(
        message,
        """
🛡️ قائمة أوامر SimoGuard

🚫 حظر | ban
🔇 كتم | mute
👢 طرد | kick

استخدم الأمر بالرد على رسالة العضو.
        """
    )


@bot.message_handler(func=lambda m: m.text in ["حظر", "ban"])
def ban_user(message):
    if not can_manage(message.from_user.id):
        bot.reply_to(message, "❌ ليس لديك صلاحية.")
        return
    if message.reply_to_message:
        try:
            bot.ban_chat_member(
                message.chat.id,
                message.reply_to_message.from_user.id
            )
            bot.reply_to(message, "🚫 تم حظر العضو.")
        except:
            bot.reply_to(
                message,
                "❌ لا أستطيع الحظر. تأكد أنني مشرف."
            )
    else:
        bot.reply_to(
            message,
            "⚠️ استخدم الأمر بالرد على رسالة العضو."
        )


@bot.message_handler(func=lambda m: m.text in ["طرد", "kick"])
def kick_user(message):
    if not can_manage(message.from_user.id):
        bot.reply_to(message, "❌ ليس لديك صلاحية.")
        return
    if message.reply_to_message:
        try:
            user_id = message.reply_to_message.from_user.id
            bot.ban_chat_member(message.chat.id, user_id)
            bot.unban_chat_member(message.chat.id, user_id)

            bot.reply_to(message, "👢 تم طرد العضو.")
        except:
            bot.reply_to(message, "❌ لا أستطيع الطرد.")
    else:
        bot.reply_to(message, "⚠️ رد على رسالة العضو.")


@bot.message_handler(func=lambda m: m.text in ["كتم", "mute"])
def mute_user(message):
    if not can_manage(message.from_user.id):
        bot.reply_to(message, "❌ ليس لديك صلاحية.")
        return
    if message.reply_to_message:
        try:
            permissions = telebot.types.ChatPermissions(
                can_send_messages=False
            )

            bot.restrict_chat_member(
                message.chat.id,
                message.reply_to_message.from_user.id,
                permissions
            )

            bot.reply_to(message, "🔇 تم كتم العضو.")
        except:
            bot.reply_to(message, "❌ لا أستطيع الكتم.")
    else:
        bot.reply_to(message, "⚠️ رد على رسالة العضو.")


bot.infinity_polling(
    timeout=60,
    long_polling_timeout=60
)
