import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🏃‍♂️ Bem-vindo à Liga da Corrida!\nEnvie sua atividade ou foto que eu registro tudo para você!")

async def photo_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📸 Foto recebida! Vou registrar como treino.")

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.PHOTO, photo_handler))

    print("Bot rodando...")
    app.run_polling()

if __name__ == "__main__":
    main()
