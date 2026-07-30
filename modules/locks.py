from permissions import can_manage


def setup_locks(bot):

    locks = {
        "روابط": False,
        "صور": False,
        "فيديو": False,
        "ملصقات": False
    }


    @bot.message_handler(func=lambda m: m.text in ["قفل الروابط", "lock links"])
    def lock_links(message):

        if not can_manage(message.from_user.id):
            bot.reply_to(message, "❌ ليس لديك صلاحية.")
            return

        locks["روابط"] = True
        bot.reply_to(message, "🔒 تم قفل الروابط.")


    @bot.message_handler(func=lambda m: m.text in ["فتح الروابط", "unlock links"])
    def unlock_links(message):

        if not can_manage(message.from_user.id):
            bot.reply_to(message, "❌ ليس لديك صلاحية.")
            return

        locks["روابط"] = False
        bot.reply_to(message, "🔓 تم فتح الروابط.")


    @bot.message_handler(func=lambda m: m.text in ["قفل الصور", "lock photo"])
    def lock_photos(message):

        if not can_manage(message.from_user.id):
            bot.reply_to(message, "❌ ليس لديك صلاحية.")
            return

        locks["صور"] = True
        bot.reply_to(message, "🔒 تم قفل الصور.")


    @bot.message_handler(func=lambda m: m.text in ["فتح الصور", "unlock photo"])
    def unlock_photos(message):

        if not can_manage(message.from_user.id):
            bot.reply_to(message, "❌ ليس لديك صلاحية.")
            return

        locks["صور"] = False
        bot.reply_to(message, "🔓 تم فتح الصور.")


    @bot.message_handler(func=lambda m: m.content_type in ["photo", "video"])
    def media_filter(message):

        if locks["صور"] and message.content_type == "photo":
            try:
                bot.delete_message(
                    message.chat.id,
                    message.message_id
                )
            except:
                pass

        if locks["فيديو"] and message.content_type == "video":
            try:
                bot.delete_message(
                    message.chat.id,
                    message.message_id
                )
            except:
                pass
