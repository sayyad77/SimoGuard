from permissions import can_manage
def setup_menu(bot):

    @bot.message_handler(func=lambda m: m.text in ["الاوامر", "menu"])
    def menu(message):

        bot.reply_to(
            message,
            """
🛡️ SimoGuard

👮 الإدارة:
حظر
طرد
كتم
فك كتم
تحذير
مسح التحذيرات

⭐ الرتب:
رفع مشرف
رفع مدير
تنزيل رتبة
المشرفين
رتبتي

🔒 القفل:
قفل الصور
قفل الفيديو
قفل الملصقات
فتح الكل

⚙️ الخدمات:
ايدي
معلومات العضو
معلومات المجموعة
القوانين

🤖 الردود:
اضف رد
حذف رد

SimoGuard 🛡️
"""
        )

    @bot.message_handler(func=lambda m: m.text in ["فتح الكل", "unlock all"])
    def unlock_all(message):

        bot.reply_to(
            message,
            "🔓 لإدارة الأقفال استخدم:\n"
            "فتح الروابط\n"
            "فتح الصور\n"
            "فتح الفيديو\n"
            "فتح الملصقات"
        )

    @bot.message_handler(func=lambda m: m.text in ["القوانين", "rules"])
    def rules(message):

        bot.reply_to(
            message,
            "📜 قوانين المجموعة:\n\n"
            "1️⃣ احترام جميع الأعضاء.\n"
            "2️⃣ يمنع السب والشتم.\n"
            "3️⃣ يمنع نشر الروابط المزعجة.\n"
            "4️⃣ يمنع إرسال محتوى مخالف.\n"
            "5️⃣ الالتزام بتعليمات الإدارة.\n\n"
            "🛡️ SimoGuard"
        )
