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

    @bot.message_handler(func=lambda m: m.text in ["معلومات المجموعة", "group info"])
    def group_info(message):

        try:
            chat = bot.get_chat(message.chat.id)
            members = bot.get_chat_member_count(message.chat.id)

            bot.reply_to(
                message,
                f"🏠 معلومات المجموعة\n\n"
                f"📌 الاسم: {chat.title}\n"
                f"🆔 المعرف: {message.chat.id}\n"
                f"👥 الأعضاء: {members}\n"
                f"🛡️ SimoGuard"
            )

        except Exception:
            bot.reply_to(message, "❌ لا أستطيع الحصول على معلومات المجموعة.")

    @bot.message_handler(func=lambda m: m.text in ["معلومات العضو", "user info"])
    def user_info(message):

        user = message.reply_to_message.from_user if message.reply_to_message else message.from_user

        try:
            member = bot.get_chat_member(
                message.chat.id,
                user.id
            )

            rank = member.status

            bot.reply_to(
                message,
                f"👤 معلومات العضو\n\n"
                f"🆔 الآيدي: {user.id}\n"
                f"👤 الاسم: {user.first_name}\n"
                f"🔖 المعرف: @{user.username if user.username else 'لا يوجد'}\n"
                f"⭐ الحالة: {rank}"
            )

        except Exception:
            bot.reply_to(message, "❌ لا أستطيع الحصول على معلومات العضو.")

    @bot.message_handler(func=lambda m: m.text in ["ايدي", "id"])
    def user_id(message):

        user = message.reply_to_message.from_user if message.reply_to_message else message.from_user

        bot.reply_to(
            message,
            f"🆔 آيدي المستخدم:\n{user.id}"
        )
