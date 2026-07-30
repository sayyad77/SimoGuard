from permissions import can_manage

rules = {}


def setup_broadcast(bot):

    @bot.message_handler(func=lambda m: m.text.startswith("وضع قوانين "))
    def set_rules(message):
        if not can_manage(message.from_user.id):
            return

        rules[message.chat.id] = message.text.replace("وضع قوانين ", "")

        bot.reply_to(message, "✅ تم حفظ القوانين.")


    @bot.message_handler(func=lambda m: m.text == "القوانين")
    def show_rules(message):

        text = rules.get(
            message.chat.id,
            "❌ لا توجد قوانين."
        )

        bot.reply_to(
            message,
            "📜 القوانين:\n" + text
        )


    @bot.message_handler(func=lambda m: m.text.startswith("إذاعة "))
    def broadcast(message):

        if not can_manage(message.from_user.id):
            return

        bot.reply_to(
            message,
            "📢 تم تنفيذ الإذاعة."
        )
