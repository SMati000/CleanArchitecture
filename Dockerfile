FROM python:3.12.0b3-alpine3.18

RUN mkdir -p /home/app

COPY . /home/app

RUN pip install python-telegram-bot
RUN pip install python-dotenv

EXPOSE 5000

CMD ["python3", "/home/app/__main__.py"]