# Mini Example of Clean Architecture

This is a really simple Telegram bot in Python, with a mini database implemented with SQLite. It is also set up to work with Docker  (Just run `docker compose up`).\
**The idea was to nicely implement Clean Architecture and good design practices, following theory as thoroughly as possible as a learning experience. The functionality itself has no real purpose, use nor sense at all.**

Even though, just to understand the code, here's an overview:
- Every interaction with the bot, lands on the *TelegramAPIHandler* class.
- You run the `/start` command, it asks you whether you want to sign in, or log in, and then asks for a username and password.
- If you chose to sign in, it saves that info in the DB. If you chose to log in, it checks that the user actually exists in the DB.
- If everything is ok, the bot replies with a confirmation message.

*Note: Some abstractions and practices (like dependency injection) could be skipped given the simplicity of the project; nevertheless they are implemented, because this project intents to be purely theory-based. In a real-life scenario, there would be a lot of trade offs between what is best design and what is best for practical purposes. *


## Screenshots

![Class Diagram](https://github.com/SMati000/CleanArchitecture/blob/main/Class%20Diagram.jpg)


## Environment Variables

To run this project, the following environment variables (to the .env file or Dockerfile) are required.

`TOKEN = your bot's Telegram token`


## Running Tests

You will find a `tests` package with few unit tests, for now. 


## Resources & Bibliography

 - [Clean Architecture Article](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)
 - [Cataloging Dependency Injection Anti-Patterns in Software Systems, University of Copenhagen, Denmark](https://arxiv.org/pdf/2109.04256.pdf)
 - Practical book: "Implementing the Clean Architecture" by Sebastian Buczynski
 - [Python Telegram API](https://docs.python-telegram-bot.org/en/stable/index.html)
 - [SQLite](https://docs.python.org/3/library/sqlite3.html)
 - [Dependency-Injector](https://python-dependency-injector.ets-labs.org/index.html)


## License

[MIT](https://choosealicense.com/licenses/mit/)

