from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext
from flask import Flask, request

app = Flask(__name__)

# Função para lidar com o comando /start
def start(update: Update, context: CallbackContext):
    keyboard = [[InlineKeyboardButton("Play", url="https://your-miniapp-url.com")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Clique no botão abaixo para jogar!', reply_markup=reply_markup)

# Configuração do bot
def main():
    updater = Updater("7227344806:AAGsi2PITxi6ab51w7WL79PsV9YLmNBWYAg", use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

# Configuração do Flask
@app.route('/')
def index():
    return 'Hello World!'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
