
from telegram import Update
from telegram.ext import ContextTypes
from telegram.constants import ParseMode



async def echo_fun(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    text = update.message.text
    text = f"<u>{text}</u>"
    await context.bot.send_message(user.id, text, parse_mode=ParseMode.HTML)

