import sys
import telebot
import discord
from discord.ext import commands as discord_commands
import threading

# استلام التوكن والآيدي
if len(sys.argv) > 1:
    TOKEN = sys.argv[1]
    ADMIN_ID = sys.argv[2] if len(sys.argv) > 2 else None
else:
    sys.exit()

# دالة تشغيل بوت تليجرام
def run_telegram():
    try:
        bot = telebot.TeleBot(TOKEN)
        @bot.message_handler(commands=['start'])
        def start(message):
            bot.reply_to(message, "✅ بوت تليجرام يعمل بنجاح!")
        bot.infinity_polling()
    except: pass

# دالة تشغيل بوت ديسكورد
def run_discord():
    try:
        intents = discord.Intents.default()
        intents.message_content = True
        bot = discord_commands.Bot(command_prefix="!", intents=intents)
        @bot.event
        async def on_ready():
            print(f"Logged in as {bot.user}")
        @bot.command()
        async def start(ctx):
            await ctx.send("✅ بوت ديسكورد يعمل بنجاح!")
        bot.run(TOKEN)
    except: pass

# تحديد نوع البوت من طول التوكن (تليجرام عادة أرقام ونقط، ديسكورد أطول)
if ":" in TOKEN:
    run_telegram()
else:
    run_discord()
