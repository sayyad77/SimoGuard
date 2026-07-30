def setup_info(bot):

    @bot.message_handler(func=lambda m: m.text in ["معلومات المجموعة", "group info"])
    def group_info(message):

        try:
            chat = bot.get_chat(message.chat.id)

            members = bot.get_chat_member_count(
                message.chat.id
            )

            bot.reply_to(
                message,
                f"""
📊 معلومات المجموعة

📌 الاسم:
{chat.title}

🆔 الايدي:
{message.chat.id}

👥 عدد الأعضاء:
{members}
"""
            )

        except:
            bot.reply_to(
                message,
                "❌ لا أستطيع جلب المعلومات."
            )
