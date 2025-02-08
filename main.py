BOT_TOKEN = ""

from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext


async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Hello! I am your bot. How can I help you?")


async def echo(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(update.message.text)


def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    print("Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()