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
