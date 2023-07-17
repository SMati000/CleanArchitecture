# Mini Example of Clean Architecture

This is a really simple Telegram bot in Python, with a mini database implemented with SQLite. It is also set up to work with Docker.\
**The idea was to nicely implement Clean Architecture and good design practices, following theory as thoroughly as possible as a learning experience. The functionality itself has no real purpose, use nor sense at all.**\
Some abstractions and practices could be skipped because of the simplicity of the project; nevertheless they are implemented, since learning was the goal as said before.\
*Note: In a real-life scenario, there would be a lot of trade offs between what is best design and what is best for practical purposes. This project intents to be purely theory-based.*


## Screenshots

![Class Diagram](https://github.com/SMati000/CleanArchitecture/blob/main/Class%20Diagram.jpg)


## Environment Variables

To run this project, the following environment variables (to the .env file or Dockerfile) are required.

`TOKEN = your bot's Telegram token`


## Running Tests

You will find a `tests` package with few unit tests, for now. 


## Resources & Bibliography

 - [Clean Architecture Article](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)
 - Practical book: "Implementing the Clean Architecture" by Sebastian Buczynski
 - [Python Telegram API](https://docs.python-telegram-bot.org/en/stable/index.html)
 - [SQLite](https://docs.python.org/3/library/sqlite3.html)


## License

[MIT](https://choosealicense.com/licenses/mit/)
