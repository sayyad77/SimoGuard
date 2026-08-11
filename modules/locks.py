from database import get_group_settings, set_group_setting
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
        set_group_setting(message.chat.id, "links", True)
        bot.reply_to(message, "🔒 تم قفل الروابط.")


    @bot.message_handler(func=lambda m: m.text in ["فتح الروابط", "unlock links"])
    def unlock_links(message):

        if not can_manage(message.from_user.id):
            bot.reply_to(message, "❌ ليس لديك صلاحية.")
            return

        locks["روابط"] = False
        set_group_setting(message.chat.id, "links", False)
        bot.reply_to(message, "🔓 تم فتح الروابط.")


    @bot.message_handler(func=lambda m: m.text in ["قفل الصور", "lock photo"])
    def lock_photos(message):

        if not can_manage(message.from_user.id):
            bot.reply_to(message, "❌ ليس لديك صلاحية.")
            return

        locks["صور"] = True
        set_group_setting(message.chat.id, "photos", True)
        bot.reply_to(message, "🔒 تم قفل الصور.")


    @bot.message_handler(func=lambda m: m.text in ["فتح الصور", "unlock photo"])
    def unlock_photos(message):

        if not can_manage(message.from_user.id):
            bot.reply_to(message, "❌ ليس لديك صلاحية.")
            return

        locks["صور"] = False
        set_group_setting(message.chat.id, "photos", False)
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

    @bot.message_handler(func=lambda m: m.text in ["قفل الفيديو", "lock video"])
    def lock_videos(message):

        if not can_manage(message.from_user.id):
            bot.reply_to(message, "❌ ليس لديك صلاحية.")
            return

        locks["فيديو"] = True
        set_group_setting(message.chat.id, "videos", True)
        bot.reply_to(message, "🔒 تم قفل الفيديو.")

    @bot.message_handler(func=lambda m: m.text in ["فتح الفيديو", "unlock video"])
    def unlock_videos(message):

        if not can_manage(message.from_user.id):
            bot.reply_to(message, "❌ ليس لديك صلاحية.")
            return

        locks["فيديو"] = False
        bot.reply_to(message, "🔓 تم فتح الفيديو.")

    @bot.message_handler(func=lambda m: m.text in ["قفل الملصقات", "lock stickers"])
    def lock_stickers(message):

        if not can_manage(message.from_user.id):
            bot.reply_to(message, "❌ ليس لديك صلاحية.")
            return

        locks["ملصقات"] = True
        set_group_setting(message.chat.id, "stickers", True)
        bot.reply_to(message, "🔒 تم قفل الملصقات.")

    @bot.message_handler(func=lambda m: m.text in ["فتح الملصقات", "unlock stickers"])
    def unlock_stickers(message):

        if not can_manage(message.from_user.id):
            bot.reply_to(message, "❌ ليس لديك صلاحية.")
            return

        locks["ملصقات"] = False
        set_group_setting(message.chat.id, "stickers", False)
        bot.reply_to(message, "🔓 تم فتح الملصقات.")

    @bot.message_handler(func=lambda m: m.text in ["حالة الأقفال", "locks status"])
    def locks_status(message):

        if not can_manage(message.from_user.id):
            bot.reply_to(message, "❌ ليس لديك صلاحية.")
            return

        links = "🔒" if locks["روابط"] else "🔓"
        photos = "🔒" if locks["صور"] else "🔓"
        videos = "🔒" if locks["فيديو"] else "🔓"
        stickers = "🔒" if locks["ملصقات"] else "🔓"

        bot.reply_to(
            message,
            "🛡️ حالة الأقفال:\n\n"
            f"{links} الروابط\n"
            f"{photos} الصور\n"
            f"{videos} الفيديو\n"
            f"{stickers} الملصقات"
        )

    @bot.message_handler(func=lambda m: m.text in ["فتح الكل", "unlock all"])
    def unlock_all(message):

        if not can_manage(message.from_user.id):
            bot.reply_to(message, "❌ ليس لديك صلاحية.")
            return

        locks["روابط"] = False
        locks["صور"] = False
        locks["فيديو"] = False
        locks["ملصقات"] = False

        bot.reply_to(
            message,
            "🔓 تم فتح جميع الأقفال."
        )
