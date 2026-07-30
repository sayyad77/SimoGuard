def setup_welcome(bot):

    welcome_status = {}

    @bot.message_handler(content_types=["new_chat_members"])
    def welcome(message):

        chat_id = message.chat.id

        if welcome_status.get(chat_id, True):

            for user in message.new_chat_members:
                bot.send_message(
                    chat_id,
                    f"""
👋 أهلاً بك {user.first_name}

🛡️ أنت الآن عضو في المجموعة.
📌 نتمنى لك وقتاً ممتعاً معنا.
"""
                )


    @bot.message_handler(func=lambda m: m.text in ["تفعيل الترحيب", "welcome on"])
    def enable_welcome(message):

        welcome_status[message.chat.id] = True

        bot.reply_to(
            message,
            "✅ تم تفعيل الترحيب."
        )


    @bot.message_handler(func=lambda m: m.text in ["تعطيل الترحيب", "welcome off"])
    def disable_welcome(message):

        welcome_status[message.chat.id] = False

        bot.reply_to(
            message,
            "❌ تم تعطيل الترحيب."
        )
