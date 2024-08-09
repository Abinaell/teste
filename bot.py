import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = '7227344806:AAGsi2PITxi6ab51w7WL79PsV9YLmNBWYAg'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Define o link do mini app
    web_app_url = 'https://funny-fox-c1ee94.netlify.app/'  # Substitua pelo URL do seu mini app

    # Cria o botão de Play com o link externo
    keyboard = [
        [InlineKeyboardButton("Play", url=web_app_url)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Envia a mensagem com o botão
    await update.message.reply_text('Pressione Play para abrir o mini app!', reply_markup=reply_markup)

async def main():
    # Cria a aplicação com o token do bot
    application = Application.builder().token(TOKEN).build()

    # Adiciona o handler para o comando /start
    application.add_handler(CommandHandler('start', start))

    # Inicia o bot
    await application.run_polling()

if __name__ == '__main__':
    try:
        # Verifica se já existe um loop de eventos rodando
        loop = asyncio.get_running_loop()
    except RuntimeError:  # Nenhum loop ativo
        loop = None

    if loop and loop.is_running():
        print("Loop de eventos já está rodando. Executando main diretamente.")
        asyncio.ensure_future(main())
    else:
        print("Iniciando novo loop de eventos.")
        asyncio.run(main())
