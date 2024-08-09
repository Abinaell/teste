from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

TOKEN = '7227344806:AAGsi2PITxi6ab51w7WL79PsV9YLmNBWYAg'

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! I am your bot.')

def main():
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
