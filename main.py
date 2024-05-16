
'''
I will check some monkey patching for some cases
This need some module from other module for checking
i used this monkey patch and the new roperty in my start_cmd function
I used the monkey patching methods so that i can use the full name's 
'''

import sys
sys.dont_write_bytecode = True

import monkey_patch


import logging

from telegram import Update
from telegram.ext import Application
from telegram.ext import CommandHandler, MessageHandler, filters

import cmd_handler
import msg_handler

def setup_logger():
    logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
    logging.getLogger("httpx").setLevel(logging.WARNING)
    return logging.getLogger(__name__)

logger = setup_logger()




"""
Here i try to add some property in the user class for checking purpose
see the monkey_patch.py there i have added the User class + new property
"""











def main() -> None:
    application = Application.builder().token("RanaUniverse🍌🍌🍌").build()

    application.add_handler(CommandHandler(
        command=["start"],
        callback=cmd_handler.start_cmd,
        filters=filters.ChatType.PRIVATE,
        block=False
    ))
    application.add_handler(CommandHandler(
        command=["cap", "help"],
        callback=cmd_handler.cap_fun,
        filters=filters.ChatType.PRIVATE,
        block=False
    ))

    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, msg_handler.echo_fun))
    application.add_handler(MessageHandler(filters.Command(), cmd_handler.extra_cmd))

    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
