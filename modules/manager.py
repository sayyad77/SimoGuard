from database import cursor, db
from permissions import is_owner


def setup_manager(bot):

    @bot.message_handler(func=lambda m: m.text in ["المشرفين", "admins"])
    def list_admins(message):

        cursor.execute(
            "SELECT user_id, rank FROM ranks"
        )

        users = cursor.fetchall()

        if not users:
            bot.reply_to(
                message,
                "📋 لا يوجد مشرفين."
            )
            return

        text = "👮 قائمة الرتب:\n\n"

        for user_id, rank in users:
            text += f"🆔 {user_id} | ⭐ {rank}\n"

        bot.reply_to(
            message,
            text
        )


    @bot.message_handler(func=lambda m: m.text in ["ايدي", "id"])
    def user_id(message):

        if message.reply_to_message:
            uid = message.reply_to_message.from_user.id

            bot.reply_to(
                message,
                f"🆔 ايدي العضو:\n{uid}"
            )
        else:
            bot.reply_to(
                message,
                f"🆔 ايديك:\n{message.from_user.id}"
            )
from database import add_rank, remove_rank
from permissions import can_change_ranks


def setup_rank_commands(bot):

    @bot.message_handler(func=lambda m: m.text in ["رفع مشرف", "رفع مدير"])
    def promote(message):

        if not can_change_ranks(message.from_user.id):
            bot.reply_to(message, "❌ ليس لديك صلاحية.")
            return

        if not message.reply_to_message:
            bot.reply_to(message, "⚠️ استخدم الأمر بالرد على العضو.")
            return

        user_id = message.reply_to_message.from_user.id

        if message.text == "رفع مدير":
            add_rank(user_id, "مدير")
        else:
            add_rank(user_id, "مشرف")

        bot.reply_to(
            message,
            "✅ تم رفع رتبة العضو."
        )


    @bot.message_handler(func=lambda m: m.text == "تنزيل رتبة")
    def demote(message):

        if not can_change_ranks(message.from_user.id):
            bot.reply_to(message, "❌ ليس لديك صلاحية.")
            return

        if not message.reply_to_message:
            bot.reply_to(message, "⚠️ استخدم الأمر بالرد.")
            return

        user_id = message.reply_to_message.from_user.id

        remove_rank(user_id)

        bot.reply_to(
            message,
            "✅ تم تنزيل الرتبة."
        )
