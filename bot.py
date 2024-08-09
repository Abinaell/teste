from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from flask import Flask, request

app = Flask(__name__)

# Token do seu bot do Telegram
TELEGRAM_TOKEN = '7227344806:AAGsi2PITxi6ab51w7WL79PsV9YLmNBWYAg'
WEB_APP_URL = 'https://funny-fox-c1ee94.netlify.app/'

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Clique no botão abaixo para iniciar o mini app!', reply_markup=telegram.ReplyKeyboardMarkup(
        [[telegram.KeyboardButton('Play', url=WEB_APP_URL)]],
        resize_keyboard=True,
        one_time_keyboard=True
    ))

def main():
    updater = Updater(TELEGRAM_TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
