from permissions import can_manage


def setup_settings(bot):

    settings = {}


    @bot.message_handler(func=lambda m: m.text in ["الاعدادات", "settings"])
    def show_settings(message):

        chat_id = message.chat.id

        data = settings.get(
            chat_id,
            {
                "protection": True,
                "links": False,
                "welcome": True
            }
        )

        bot.reply_to(
            message,
            f"""
⚙️ إعدادات المجموعة:

🛡️ الحماية: {"مفعلة" if data["protection"] else "معطلة"}
🔗 الروابط: {"مقفلة" if data["links"] else "مفتوحة"}
👋 الترحيب: {"مفعل" if data["welcome"] else "معطل"}
"""
        )


    @bot.message_handler(func=lambda m: m.text in ["تفعيل الحماية", "protection on"])
    def enable_protection(message):

        if not can_manage(message.from_user.id):
            bot.reply_to(message, "❌ ليس لديك صلاحية.")
            return

        settings.setdefault(
            message.chat.id,
            {}
        )["protection"] = True

        bot.reply_to(message, "✅ تم تفعيل الحماية.")


    @bot.message_handler(func=lambda m: m.text in ["تعطيل الحماية", "protection off"])
    def disable_protection(message):

        if not can_manage(message.from_user.id):
            bot.reply_to(message, "❌ ليس لديك صلاحية.")
            return

        settings.setdefault(
            message.chat.id,
            {}
        )["protection"] = False

        bot.reply_to(message, "❌ تم تعطيل الحماية.")
