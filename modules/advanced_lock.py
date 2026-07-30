from permissions import can_manage


def setup_advanced_lock(bot):

    locks = {
        "links": set(),
        "photo": set(),
        "video": set(),
        "sticker": set()
    }


    @bot.message_handler(func=lambda m: m.text in [
        "قفل الروابط",
        "قفل الصور",
        "قفل الفيديو",
        "قفل الملصقات"
    ])
    def lock_type(message):

        if not can_manage(message.from_user.id):
            bot.reply_to(message, "❌ ليس لديك صلاحية.")
            return

        chat_id = message.chat.id

        if "الروابط" in message.text:
            locks["links"].add(chat_id)

        elif "الصور" in message.text:
            locks["photo"].add(chat_id)

        elif "الفيديو" in message.text:
            locks["video"].add(chat_id)

        elif "الملصقات" in message.text:
            locks["sticker"].add(chat_id)

        bot.reply_to(message, "🔒 تم القفل.")


    @bot.message_handler(func=lambda m: m.text in [
        "فتح الروابط",
        "فتح الصور",
        "فتح الفيديو",
        "فتح الملصقات",
        "فتح الكل"
    ])
    def unlock_type(message):

        if not can_manage(message.from_user.id):
            bot.reply_to(message, "❌ ليس لديك صلاحية.")
            return

        chat_id = message.chat.id

        if message.text == "فتح الكل":
            for lock in locks.values():
                lock.discard(chat_id)
        else:
            if "الروابط" in message.text:
                locks["links"].discard(chat_id)

            elif "الصور" in message.text:
                locks["photo"].discard(chat_id)

            elif "الفيديو" in message.text:
                locks["video"].discard(chat_id)

            elif "الملصقات" in message.text:
                locks["sticker"].discard(chat_id)

        bot.reply_to(message, "🔓 تم الفتح.")


    @bot.message_handler(content_types=[
        "photo",
        "video",
        "sticker"
    ])
    def media_lock(message):

        chat_id = message.chat.id

        try:
            if message.photo and chat_id in locks["photo"]:
                bot.delete_message(chat_id, message.message_id)

            elif message.video and chat_id in locks["video"]:
                bot.delete_message(chat_id, message.message_id)

            elif message.sticker and chat_id in locks["sticker"]:
                bot.delete_message(chat_id, message.message_id)

        except:
            pass
