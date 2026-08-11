from collections import defaultdict
from permissions import can_manage


def setup_warnings(bot):

    warnings = defaultdict(int)


    @bot.message_handler(func=lambda m: m.text in ["تحذير", "warn"])
    def warn_user(message):

        if not can_manage(message.from_user.id):
            bot.reply_to(message, "❌ ليس لديك صلاحية.")
            return

        if not message.reply_to_message:
            bot.reply_to(message, "⚠️ استخدم الأمر بالرد على العضو.")
            return

        user_id = message.reply_to_message.from_user.id

        warnings[user_id] += 1

        bot.reply_to(
            message,
            f"⚠️ تم تحذير العضو.\n"
            f"عدد التحذيرات: {warnings[user_id]}"
        )


    @bot.message_handler(func=lambda m: m.text in ["تحذيراتي", "mywarns"])
    def my_warns(message):

        count = warnings[message.from_user.id]

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

        warnings[user_id] = 0

        bot.reply_to(
            message,
            "✅ تم مسح تحذيرات العضو."
        )

    @bot.message_handler(func=lambda m: m.text in ["حظر عند 3", "warnban"])
    def warn_ban(message):

        if not can_manage(message.from_user.id):
            bot.reply_to(message, "❌ ليس لديك صلاحية.")
            return

        if not message.reply_to_message:
            bot.reply_to(message, "⚠️ استخدم الأمر بالرد على العضو.")
            return

        user_id = message.reply_to_message.from_user.id

        if warnings[user_id] >= 3:
            try:
                bot.ban_chat_member(message.chat.id, user_id)
                warnings[user_id] = 0
                bot.reply_to(message, "🚫 تم حظر العضو بعد 3 تحذيرات.")
            except Exception:
                bot.reply_to(message, "❌ لا أستطيع حظر العضو.")
        else:
            bot.reply_to(
                message,
                f"⚠️ تحذيرات العضو: {warnings[user_id]}\n"
                f"🚫 يحتاج إلى 3 تحذيرات للحظر."
            )
