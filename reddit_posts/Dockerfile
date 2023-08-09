# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8.3

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements
COPY requirements.txt .
COPY scrape.py scrape.py
RUN python -m pip install -r requirements.txt

WORKDIR /app
COPY . /app

#cron job
RUN apt-get update && apt-get -y install cron vim

COPY crontab /etc/cron.d/crontab

RUN chmod 0644 /etc/cron.d/crontab
RUN crontab /etc/cron.d/crontab

CMD ["cron", "-f"]