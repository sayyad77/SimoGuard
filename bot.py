import telebot
from config import BOT_TOKEN, OWNER_ID
from modules.ranks import setup_ranks
from modules.admin import setup_admin
from modules.tools import setup_tools
from modules.locks import setup_locks
from modules.welcome import setup_welcome
from modules.replies import setup_replies
from modules.settings import setup_settings
from modules.security import setup_security
from modules.warnings import setup_warnings
from modules.manager import setup_manager
from modules.manager import setup_rank_commands
from modules.info import setup_info
from modules.advanced_lock import setup_advanced_lock
from modules.extras import setup_extras
from modules.broadcast import setup_broadcast
from modules.menu import setup_menu
bot = telebot.TeleBot(BOT_TOKEN)
setup_ranks(bot)
setup_admin(bot)
setup_tools(bot)
setup_locks(bot)
setup_welcome(bot)
setup_replies(bot)
setup_settings(bot)
setup_security(bot)
setup_warnings(bot)
setup_manager(bot)
setup_rank_commands(bot)
setup_info(bot)
setup_advanced_lock(bot)
setup_extras(bot)
setup_broadcast(bot)
setup_menu(bot)
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

bot.remove_webhook(drop_pending_updates=True)
bot.infinity_polling()

