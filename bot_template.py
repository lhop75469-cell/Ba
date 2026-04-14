import telebot
import sys

# استلام التوكن والآيدي من الواجهة
if len(sys.argv) > 1:
    BOT_TOKEN = sys.argv[1]
    ADMIN_ID = sys.argv[2] if len(sys.argv) > 2 else None
else:
    print("No token provided!")
    sys.exit()

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "✅ أهلاً بك! بوتك الآن يعمل بنجاح من خلال سيرفر Render الخاص بك.")

print("البوت بدأ العمل...")
bot.infinity_polling()
