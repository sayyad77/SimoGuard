from database import add_reply, delete_reply, get_reply
from database import add_reply, delete_reply, get_reply
from permissions import can_manage


def setup_replies(bot):

    @bot.message_handler(func=lambda m: m.text.startswith("اضف رد "))
    def add_new_reply(message):

        if not can_manage(message.from_user.id):
            bot.reply_to(message, "❌ ليس لديك صلاحية.")
            return

        try:
            data = message.text.replace("اضف رد ", "", 1)
            parts = data.split("|")

            trigger = parts[0].strip()
            response = parts[1].strip()

            add_reply(trigger, response)

            bot.reply_to(
                message,
                "✅ تم إضافة الرد."
            )

        except:
            bot.reply_to(
                message,
                "⚠️ الاستخدام:\nاضف رد السؤال | الجواب"
            )


    @bot.message_handler(func=lambda m: m.text.startswith("حذف رد "))
    def remove_reply(message):

        if not can_manage(message.from_user.id):
            bot.reply_to(message, "❌ ليس لديك صلاحية.")
            return

        trigger = message.text.replace("حذف رد ", "", 1)

        delete_reply(trigger)

        bot.reply_to(
            message,
            "✅ تم حذف الرد."
        )


    @bot.message_handler(func=lambda m: False)
    def auto_reply(message):

        if not message.text:
            return

        response = get_reply(message.text)

        if response:
            bot.reply_to(
                message,
                response
            )

    @bot.message_handler(func=lambda m: m.text and m.text.startswith("اضف رد "))
    def add_auto_reply(message):

        if not can_manage(message.from_user.id):
            bot.reply_to(message, "❌ ليس لديك صلاحية.")
            return

        data = message.text.replace("اضف رد ", "", 1).split("|", 1)

        if len(data) != 2:
            bot.reply_to(message, "⚠️ استخدم:\nاضف رد الكلمة | الرد")
            return

        trigger = data[0].strip()
        response = data[1].strip()

        add_reply(trigger, response)

        bot.reply_to(message, "✅ تم إضافة الرد التلقائي.")


    @bot.message_handler(func=lambda m: m.text and m.text.startswith("حذف رد "))
    def delete_auto_reply(message):

        if not can_manage(message.from_user.id):
            bot.reply_to(message, "❌ ليس لديك صلاحية.")
            return

        trigger = message.text.replace("حذف رد ", "", 1).strip()

        delete_reply(trigger)

        bot.reply_to(message, "🗑️ تم حذف الرد التلقائي.")
