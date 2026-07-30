import telebot
from permissions import can_manage


def setup_tools(bot):

    @bot.message_handler(func=lambda m: m.text in ["ايدي", "id"])
    def user_id(message):
        if message.reply_to_message:
            user = message.reply_to_message.from_user

            bot.reply_to(
                message,
                f"🆔 الايدي:\n{user.id}\n\n👤 الاسم:\n{user.first_name}"
            )
        else:
            bot.reply_to(
                message,
                f"🆔 ايديك:\n{message.from_user.id}"
            )


    @bot.message_handler(func=lambda m: m.text in ["معلومات", "info"])
    def user_info(message):

        if message.reply_to_message:
            user = message.reply_to_message.from_user

            bot.reply_to(
                message,
                f"""
👤 معلومات العضو:

الاسم: {user.first_name}
الايدي: {user.id}
"""
            )
        else:
            bot.reply_to(
                message,
                "⚠️ استخدم الأمر بالرد على العضو."
            )


    @bot.message_handler(func=lambda m: m.text in ["مسح", "delete"])
    def delete_message(message):

        if not can_manage(message.from_user.id):
            bot.reply_to(message, "❌ ليس لديك صلاحية.")
            return

        if message.reply_to_message:
            try:
                bot.delete_message(
                    message.chat.id,
                    message.reply_to_message.message_id
                )

                bot.delete_message(
                    message.chat.id,
                    message.message_id
                )

            except:
                bot.reply_to(
                    message,
                    "❌ لا أستطيع حذف الرسالة."
                )
        else:
            bot.reply_to(
                message,
                "⚠️ استخدم الأمر بالرد."
            )


    @bot.message_handler(func=lambda m: m.text in ["تنظيف", "clean"])
    def clean(message):

        if not can_manage(message.from_user.id):
            bot.reply_to(message, "❌ ليس لديك صلاحية.")
            return

        bot.reply_to(
            message,
            "🧹 سيتم إضافة التنظيف الكامل لاحقاً."
        )
