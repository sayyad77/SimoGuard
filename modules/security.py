import time
from collections import defaultdict
from permissions import can_manage


def setup_security(bot):

    spam = defaultdict(list)
    warnings = defaultdict(int)

    protection = {}


    @bot.message_handler(func=lambda m: m.text in ["تفعيل الحماية", "protection on"])
    def enable_security(message):

        if not can_manage(message.from_user.id):
            bot.reply_to(message, "❌ ليس لديك صلاحية.")
            return

        protection[message.chat.id] = True

        bot.reply_to(
            message,
            "🛡️ تم تفعيل الحماية."
        )


    @bot.message_handler(func=lambda m: m.text in ["تعطيل الحماية", "protection off"])
    def disable_security(message):

        if not can_manage(message.from_user.id):
            bot.reply_to(message, "❌ ليس لديك صلاحية.")
            return

        protection[message.chat.id] = False

        bot.reply_to(
            message,
            "❌ تم تعطيل الحماية."
        )


    @bot.message_handler(func=lambda m: False)
    def anti_spam(message):

        if not protection.get(message.chat.id, False):
            return

        if not message.text:
            return

        user = message.from_user.id
        now = time.time()

        spam[user].append(now)

        spam[user] = [
            x for x in spam[user]
            if now - x < 5
        ]

        if len(spam[user]) >= 5:

            warnings[user] += 1

            try:
                bot.delete_message(
                    message.chat.id,
                    message.message_id
                )
            except:
                pass

            bot.send_message(
                message.chat.id,
                f"⚠️ تم تحذير العضو.\nالإنذارات: {warnings[user]}"
            )

            spam[user] = []
