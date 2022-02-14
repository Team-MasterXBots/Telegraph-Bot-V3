FROM python:3.8-slim-buster

RUN apt update && apt upgrade -y
COPY bot.py /start
CMD ["/bin/bash", "/start"]
