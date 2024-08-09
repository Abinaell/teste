from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Updater, CommandHandler, CallbackContext

TOKEN = '7227344806:AAGsi2PITxi6ab51w7WL79PsV9YLmNBWYAg'

def start(update: Update, context: CallbackContext) -> None:
    # Define o link do mini app
    web_app_url = 'https://funny-fox-c1ee94.netlify.app/'  # Substitua pelo URL do seu mini app

    # Cria o botão de Play com o WebApp
    keyboard = [
        [InlineKeyboardButton("Play", web_app=WebAppInfo(url=web_app_url))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Envia a mensagem com o botão
    update.message.reply_text('Pressione Play para abrir o mini app!', reply_markup=reply_markup)

def main():
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    # Adiciona o handler para o comando /start
    dispatcher.add_handler(CommandHandler('start', start))

    # Inicia o bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
