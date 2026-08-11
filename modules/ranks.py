from database import add_rank, remove_rank, get_rank
from config import OWNER_ID
from permissions import can_change_ranks


def setup_ranks(bot):

    @bot.message_handler(func=lambda m: m.text in ["رتبتي", "myrank"])
    def my_rank(message):
        rank = get_rank(message.from_user.id)

        if rank:
            bot.reply_to(message, f"⭐ رتبتك: {rank}")
        else:
            bot.reply_to(message, "❌ لا توجد لديك رتبة.")


    def set_rank(message, rank_name):

        if not can_change_ranks(message.from_user.id):
            bot.reply_to(message, "❌ ليس لديك صلاحية.")
            return

        if not message.reply_to_message:
            bot.reply_to(message, "⚠️ استخدم الأمر بالرد على العضو.")
            return

        user_id = message.reply_to_message.from_user.id

        add_rank(user_id, rank_name)

        bot.reply_to(
            message,
            f"✅ تم رفع العضو إلى رتبة: {rank_name}"
        )


    @bot.message_handler(func=lambda m: m.text == "رفع مدير")
    def add_manager(message):
        set_rank(message, "مدير")


    @bot.message_handler(func=lambda m: m.text == "رفع مشرف")
    def add_supervisor(message):
        set_rank(message, "مشرف")


    @bot.message_handler(func=lambda m: m.text == "رفع منشئ")
    def add_creator(message):
        set_rank(message, "منشئ")


    @bot.message_handler(func=lambda m: m.text == "رفع مالك")
    def add_owner(message):
        set_rank(message, "مالك")


    @bot.message_handler(func=lambda m: m.text in ["تنزيل رتبة", "تنزيل"])
    def remove_user_rank(message):

        if not can_change_ranks(message.from_user.id):
            bot.reply_to(message, "❌ ليس لديك صلاحية.")
            return

        if message.reply_to_message:
            user_id = message.reply_to_message.from_user.id

            remove_rank(user_id)

            bot.reply_to(message, "✅ تم تنزيل رتبة العضو.")
        else:
            bot.reply_to(message, "⚠️ استخدم الأمر بالرد.")

    @bot.message_handler(func=lambda m: m.text in ["رتبتي", "my rank"])
    def my_rank(message):

        from permissions import get_user_rank

        rank = get_user_rank(message.from_user.id)

        bot.reply_to(
            message,
            f"⭐ رتبتك: {rank or 'عضو'}"
        )
