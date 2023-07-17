from infrastructure import AccessController
import functools
import logging
import os
from typing import Dict
from html import escape
from uuid import uuid4

from dotenv import load_dotenv
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup, \
    InlineQueryResultArticle, InputTextMessageContent, Update
from telegram.constants import ParseMode
from telegram.ext import Application, CommandHandler, MessageHandler, ConversationHandler, \
    filters, PicklePersistence, CallbackQueryHandler, InlineQueryHandler, ContextTypes

from infrastructure.AccessPresenter import AccessPresenter, PresenterI


class TelegramAPIHandler:
    TOKEN: str

    PORT: int
    
    USERNAME: int
    PASSWORD: int
    DONE: int

    logger: logging.Logger
    
    mode: AccessController.Mode
    tempUsername: str
    tempPassword: str


    def __init__(self):
        load_dotenv()
        self.PORT = int(os.environ.get('PORT', 5000))

        # Enable logging
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                            level=logging.INFO)
        self.logger = logging.getLogger(__name__)

        self.TOKEN = os.environ["TOKEN"]
        self.USERNAME, self.PASSWORD, self.DONE = range(3)


    async def start(self, update, context) -> int:
        reply_keyboard = [["Log In"], ["Sign Up"]]

        await update.message.reply_text(
            "Hi! Do you want to log in, or sign up?",
            reply_markup=ReplyKeyboardMarkup(
                reply_keyboard, one_time_keyboard=True),
        )

        return self.USERNAME


    async def username(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        self.mode = AccessController.Mode(update.message.text == "Sign Up")
        
        await update.message.reply_text(
            "I see! Please tell me your username",
            reply_markup=ReplyKeyboardRemove(),
        )

        return self.PASSWORD


    async def password(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        self.tempUsername = update.message.text

        await update.message.reply_text(
            "Now, your password!",
        )

        return self.DONE


    async def done(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        self.tempPassword = update.message.text

        c = AccessController.AccessController(self.tempUsername, self.tempPassword)
        c.access(self.mode)

        presenter: PresenterI
        presenter = AccessPresenter()
        presenter.present(c.getMessage())

        await update.message.reply_html(
            presenter.getViewModel()
        )

        return ConversationHandler.END


    def local(self):
        application = Application.builder().token(self.TOKEN).build()
        
        conv_handler = ConversationHandler(
            entry_points=[CommandHandler("start", self.start)],
            states={
                self.USERNAME: [MessageHandler(filters.Regex("^(Sign Up|Log In)$"), self.username)],
                self.PASSWORD: [MessageHandler(filters.TEXT, self.password)],
                self.DONE: [MessageHandler(filters.TEXT, self.done)],
            },
            fallbacks=[],
        )

        application.add_handler(conv_handler)
        application.run_polling(allowed_updates=Update.ALL_TYPES)