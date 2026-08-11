from permissions import can_manage
from database import get_warnings, set_warnings, clear_warnings


def setup_warnings(bot):

    @bot.message_handler(func=lambda m: m.text in ["تحذير", "warn"])
    def warn_user(message):

        if not can_manage(message.from_user.id):
            bot.reply_to(message, "❌ ليس لديك صلاحية.")
            return

        if not message.reply_to_message:
            bot.reply_to(message, "⚠️ استخدم الأمر بالرد على العضو.")
            return

        user_id = message.reply_to_message.from_user.id
        count = get_warnings(message.chat.id, user_id) + 1

        set_warnings(message.chat.id, user_id, count)

        bot.reply_to(
            message,
            f"⚠️ تم تحذير العضو.\n"
            f"عدد التحذيرات: {count}"
        )


    @bot.message_handler(func=lambda m: m.text in ["تحذيراتي", "mywarns"])
    def my_warns(message):

        count = get_warnings(
            message.chat.id,
            message.from_user.id
        )

        bot.reply_to(
            message,
            f"⚠️ تحذيراتك: {count}"
        )


    @bot.message_handler(func=lambda m: m.text in ["مسح التحذيرات", "clearwarn"])
    def clear_warns(message):

        if not can_manage(message.from_user.id):
            bot.reply_to(message, "❌ ليس لديك صلاحية.")
            return

        if not message.reply_to_message:
            bot.reply_to(message, "⚠️ استخدم الأمر بالرد.")
            return

        user_id = message.reply_to_message.from_user.id

        clear_warnings(message.chat.id, user_id)

        bot.reply_to(
            message,
            "✅ تم مسح تحذيرات العضو."
        )
