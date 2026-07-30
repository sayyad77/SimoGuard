from permissions import can_manage


def setup_extras(bot):

    @bot.message_handler(func=lambda m: m.text in ["مسح", "delete"])
    def delete_msg(message):

        if not can_manage(message.from_user.id):
            return

        try:
            bot.delete_message(
                message.chat.id,
                message.message_id
            )
        except:
            pass


    @bot.message_handler(func=lambda m: m.text in ["طرد", "kick"])
    def kick(message):

        if not can_manage(message.from_user.id):
            bot.reply_to(message, "❌ ليس لديك صلاحية.")
            return

        if not message.reply_to_message:
            bot.reply_to(message, "⚠️ رد على العضو.")
            return

        user_id = message.reply_to_message.from_user.id

        try:
            bot.ban_chat_member(message.chat.id, user_id)
            bot.unban_chat_member(message.chat.id, user_id)

            bot.reply_to(message, "👢 تم الطرد.")
        except:
            bot.reply_to(message, "❌ فشل الطرد.")


    @bot.message_handler(func=lambda m: m.text in ["معلومات العضو", "userinfo"])
    def user_info(message):

        user = message.reply_to_message.from_user if message.reply_to_message else message.from_user

        bot.reply_to(
            message,
            f"""
👤 معلومات العضو

الاسم: {user.first_name}
🆔 الايدي: {user.id}
"""
        )
