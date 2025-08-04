from telegram.ext import Updater, CommandHandler
import os

# تأكد أنك أضفت متغير البيئة BOT_TOKEN في لوحة Render
TOKEN = os.getenv("BOT_TOKEN")

def start(update, context):
    update.message.reply_text("مرحباً! أنا بوتك.")

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))
updater.start_polling()
updater.idle()