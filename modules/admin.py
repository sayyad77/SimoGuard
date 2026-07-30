import telebot
from permissions import can_manage


def setup_admin(bot):

    @bot.message_handler(func=lambda m: m.text in ["حظر", "ban"])
    def ban_user(message):

        if not can_manage(message.from_user.id):
            bot.reply_to(message, "❌ ليس لديك صلاحية.")
            return

        if message.reply_to_message:
            try:
                user_id = message.reply_to_message.from_user.id
                bot.ban_chat_member(message.chat.id, user_id)
                bot.reply_to(message, "🚫 تم حظر العضو.")
            except:
                bot.reply_to(message, "❌ لا أستطيع الحظر.")
        else:
            bot.reply_to(message, "⚠️ استخدم الأمر بالرد.")


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
            bot.reply_to(message, "⚠️ استخدم الأمر بالرد.")


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
            bot.reply_to(message, "⚠️ استخدم الأمر بالرد.")


    @bot.message_handler(func=lambda m: m.text in ["فك كتم", "unmute"])
    def unmute_user(message):

        if not can_manage(message.from_user.id):
            bot.reply_to(message, "❌ ليس لديك صلاحية.")
            return

        if message.reply_to_message:
            try:
                permissions = telebot.types.ChatPermissions(
                    can_send_messages=True,
                    can_send_media_messages=True
                )

                bot.restrict_chat_member(
                    message.chat.id,
                    message.reply_to_message.from_user.id,
                    permissions
                )

                bot.reply_to(message, "🔊 تم فك الكتم.")
            except:
                bot.reply_to(message, "❌ لا أستطيع فك الكتم.")
        else:
            bot.reply_to(message, "⚠️ استخدم الأمر بالرد.")
