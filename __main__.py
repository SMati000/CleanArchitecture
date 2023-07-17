from outter.SQLiteHandler import SQLiteHandler
from outter.TelegramAPIHandler import TelegramAPIHandler

if __name__ == '__main__':
    db = SQLiteHandler()

    tg = TelegramAPIHandler()
    tg.local()