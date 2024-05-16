
'''
This is a module which allow user /start to user
'''

from telegram import Update
from telegram.ext import ContextTypes
from telegram.constants import ParseMode


async def extra_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    text = update.message.text
    text = f"<code>{text}</code>"
    await context.bot.send_message(user.id, text, parse_mode=ParseMode.HTML)


async def start_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    text = (f"Full Name Inbuild: <b><u>{user.full_name_html}</u></b>\n")
    text += (f"Full Name Cap <b><u>{user.full_name_cap}</u></b>\n")
    text += f"Your double name is: {user.name_double}\n"
    text += f"Your name length is: {user.name_char_count}\n"
    text += f"Your Fancy Name is: {user.double_string}"
    await context.bot.send_message(user.id, text, parse_mode=ParseMode.HTML)





async def cap_fun(update: Update, context: ContextTypes.DEFAULT_TYPE):
    '''/cap when someone send'''
    user = update.message.from_user
    await context.bot.send_message(user.id, f"{user.full_name}")
    await context.bot.send_message(user.id, f"{user.full_name_cap}")





