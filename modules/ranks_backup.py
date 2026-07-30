from database import add_rank, remove_rank, get_rank
from config import OWNER_ID


def setup_ranks(bot):

    @bot.message_handler(func=lambda m: m.text in ["رتبتي", "myrank"])
    def my_rank(message):
        rank = get_rank(message.from_user.id)

        if rank:
            bot.reply_to(
                message,
                f"⭐ رتبتك: {rank}"
            )
        else:
            bot.reply_to(
                message,
                "❌ لا توجد لديك رتبة."
            )


    @bot.message_handler(func=lambda m: m.text in ["رفع مدير", "add manager"])
    def add_manager(message):

        if message.from_user.id != OWNER_ID:
            return

        if message.reply_to_message:
            user_id = message.reply_to_message.from_user.id

            add_rank(user_id, "مدير")

            bot.reply_to(
                message,
                "🔰 تم رفع العضو مدير."
            )
        else:
            bot.reply_to(
                message,
                "⚠️ استخدم الأمر بالرد على العضو."
            )


    @bot.message_handler(func=lambda m: m.text in ["تنزيل رتبة", "remove rank"])
    def remove_user_rank(message):

        if message.from_user.id != OWNER_ID:
            return

        if message.reply_to_message:
            user_id = message.reply_to_message.from_user.id

            remove_rank(user_id)

            bot.reply_to(
                message,
                "✅ تم تنزيل الرتبة."
            )
        else:
            bot.reply_to(
                message,
                "⚠️ استخدم الأمر بالرد."
            )
