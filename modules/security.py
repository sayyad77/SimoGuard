from database import get_group_settings, set_group_setting
import time
from collections import defaultdict
from permissions import can_manage


def setup_security(bot):

    spam = defaultdict(list)
    warnings = defaultdict(int)
    protection = {}

    @bot.message_handler(
        func=lambda m: m.text in ["تفعيل الحماية", "protection on"]
    )
    def enable_security(message):

        if not can_manage(message.from_user.id):
            bot.reply_to(message, "❌ ليس لديك صلاحية.")
            return

        protection[message.chat.id] = True
        set_group_setting(message.chat.id, "protection", True)

        bot.reply_to(
            message,
            "🛡️ تم تفعيل الحماية."
        )

    @bot.message_handler(
        func=lambda m: m.text in ["تعطيل الحماية", "protection off"]
    )
    def disable_security(message):

        if not can_manage(message.from_user.id):
            bot.reply_to(message, "❌ ليس لديك صلاحية.")
            return

        protection[message.chat.id] = False
        set_group_setting(message.chat.id, "protection", False)

        bot.reply_to(
            message,
            "🔓 تم تعطيل الحماية."
        )

    @bot.message_handler(func=lambda m: True)
    def anti_spam(message):

        if not protection.get(message.chat.id, False):
            return

        if not message.from_user:
            return

        # تجاهل أوامر المشرفين
        if can_manage(message.from_user.id):
            return

        user_id = message.from_user.id
        now = time.time()

        spam_key = (message.chat.id, user_id)

        spam[spam_key].append(now)

        spam[spam_key] = [
            x for x in spam[spam_key]
            if now - x < 5
        ]

        if len(spam[spam_key]) >= 5:

            warnings[spam_key] += 1

            try:
                bot.delete_message(
                    message.chat.id,
                    message.message_id
                )
            except Exception:
                pass

            count = warnings[spam_key]

            bot.send_message(
                message.chat.id,
                f"⚠️ تم تحذير العضو.\n"
                f"الإنذارات: {count}"
            )

            spam[spam_key] = []

    @bot.message_handler(func=lambda m: m.text in ["حالة الحماية", "security status"])
    def security_status(message):

        if not can_manage(message.from_user.id):
            bot.reply_to(message, "❌ ليس لديك صلاحية.")
            return

        status = "🟢 مفعلة" if protection.get(message.chat.id, False) else "🔴 معطلة"

        bot.reply_to(
            message,
            f"🛡️ حالة الحماية: {status}"
        )

    @bot.message_handler(func=lambda m: m.chat.type in ["group", "supergroup"])
    def load_saved_protection(message):

        if message.chat.id not in protection:
            settings = get_group_settings(message.chat.id)
            protection[message.chat.id] = settings["protection"]

    @bot.message_handler(func=lambda m: m.chat.type in ["group", "supergroup"])
    def spam_action(message):

        if not protection.get(message.chat.id, False):
            return

        user_id = message.from_user.id

        if warnings[user_id] >= 3:
            try:
                permissions = telebot.types.ChatPermissions(
                    can_send_messages=False
                )

                bot.restrict_chat_member(
                    message.chat.id,
                    user_id,
                    permissions
                )

                bot.send_message(
                    message.chat.id,
                    "🔇 تم كتم العضو بسبب تكرار السبام."
                )

                warnings[user_id] = 0

            except:
                pass
