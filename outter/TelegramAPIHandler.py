import functools
from dependency_injector import providers
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

from infrastructure.AccessController import Mode
from infrastructure.AccessPresenter import AccessPresenter, PresenterI
from DependenciesContainer import Container


class TelegramAPIHandler:
    """
    This class is listening for bot activity, and replying accordingly through the Telegram API.

    Attributes
    -----------
    TOKEN: str
        the Telegram's bot token
    PORT: int
        the port in which the bot will be listening
    USERNAME, PASSWORD, DONE: int
        the states in which the start conversation can be.
    mode: AccessController.Mode (@dataclass)
        indicates whether the user wants to sign in or log in
    tempUsername, tempPassword: str
        saves username and password temporarily

    Methods
    ----------
    start(update, context) -> int:
        this is the method that is called when you run '/start' in the bot and
        asks for the mode (log in/sign in) 
    username(update, context) -> int:
        this method runs after start(update, context), and asks for the username 
    password(update, context) -> int:
        this method runs after username(update, context), and asks for the password
    done(update, context) -> int:
        runs after password(update, context), replies with a confirmation message, and ends the conversation
    local():
        sets the bot up and running
    """

    TOKEN: str

    PORT: int
    
    USERNAME: int
    PASSWORD: int
    DONE: int

    logger: logging.Logger
    
    mode: Mode
    tempUsername: str
    tempPassword: str


    def __init__(self):
        """
        inits the variables
        """
        load_dotenv()
        self.PORT = int(os.environ.get('PORT', 5000))

        # Enable logging
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                            level=logging.INFO)
        self.logger = logging.getLogger(__name__)

        self.TOKEN = os.environ["TOKEN"]
        self.USERNAME, self.PASSWORD, self.DONE = range(3)


    async def start(self, update, context) -> int:
        """
        When someone sends /start to the bot, this method is called and asks for the mode (log in/sign in)
        It is called by the conversation handler startConvo.

        parameters
        -----------
        update: telegram.Update
            represents an incoming update
        context: telegram.ext.ContextTypes
            context object passed to the callback

        return
        ---------
        state: int
            state in which the conversation will be. It tells the conversation handler what to do next; 
            in this case, call the username(update, context) method
        """

        reply_keyboard = [["Log In"], ["Sign Up"]]

        await update.message.reply_text(
            "Hi! Do you want to log in, or sign up?",
            reply_markup=ReplyKeyboardMarkup(
                reply_keyboard, one_time_keyboard=True),
        )

        return self.USERNAME


    async def username(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        """
        It is called after the start(update, context) method, and asks for the username.

        parameters
        -----------
        update: telegram.Update
            represents an incoming update
        context: telegram.ext.ContextTypes
            context object passed to the callback

        return
        ---------
        state: int
            state in which the conversation will be. It tells the conversation handler what to do next; 
            in this case, call the password(update, context) method
        """

        self.mode = Mode(update.message.text == "Sign Up")
        
        await update.message.reply_text(
            "I see! Please tell me your username",
            reply_markup=ReplyKeyboardRemove(),
        )

        return self.PASSWORD


    async def password(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        """
        It is called after the username(update, context) method, and asks for the password.

        parameters
        -----------
        update: telegram.Update
            represents an incoming update
        context: telegram.ext.ContextTypes
            context object passed to the callback

        return
        ---------
        state: int
            state in which the conversation will be. It tells the conversation handler what to do next; 
            in this case, call the done(update, context) method
        """

        self.tempUsername = update.message.text

        await update.message.reply_text(
            "Now, your password!",
        )

        return self.DONE


    async def done(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        """
        It is called after the password(update, context) method, replies to the user and ends the conversation.

        parameters
        -----------
        update: telegram.Update
            represents an incoming update
        context: telegram.ext.ContextTypes
            context object passed to the callback

        return
        ---------
        state: int
            state in which the conversation will be. It tells the conversation handler what to do next; 
            in this case, end the conversation
        """

        self.tempPassword = update.message.text

        c = Container().sAccessController(
            username = self.tempUsername, password = self.tempPassword
        )
        c.access(self.mode)

        presenter: PresenterI
        presenter = AccessPresenter()
        presenter.present(c.getMessage())

        await update.message.reply_html(
            presenter.getViewModel()
        )

        return ConversationHandler.END


    def local(self):
        """
        Sets the bot up and running

        Creates the application and the handlers, adds them to the application, and then starts the bot.
        """

        application = Application.builder().token(self.TOKEN).build()
        
        startConvo = ConversationHandler(
            entry_points=[CommandHandler("start", self.start)],
            states={
                self.USERNAME: [MessageHandler(filters.Regex("^(Sign Up|Log In)$"), self.username)],
                self.PASSWORD: [MessageHandler(filters.TEXT, self.password)],
                self.DONE: [MessageHandler(filters.TEXT, self.done)],
            },
            fallbacks=[],
        )

        application.add_handler(startConvo)
        application.run_polling(allowed_updates=Update.ALL_TYPES)