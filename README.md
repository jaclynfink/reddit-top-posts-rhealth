# reddit-top-posts-rhealth

## Table of Contents

- [Description](#description)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Cron Job](#cron-job)
- [Dependencies](#dependencies)
- [Dashboard](#dashboard)

## Description

This project is a Dockerized Python script that uses the Reddit API to scrape top posts from the "health" subreddit. It performs natural language processing (NLP) analysis on the post titles using scispaCy, extracts relevant information, and stores the data in a PostgreSQL database.

## Getting Started

### Prerequisites

- Docker
- Docker Compose

### Installation

1. Clone this repository to your local machine.

   ```sh
   git clone https://github.com/jaclynfink/reddit-top-posts-rhealth.git
   ```

2. Create a credentials.env file in the root directory and fill it with your Reddit API and PostgreSQL database credentials.
```
CLIENT_ID=your_reddit_client_id
CLIENT_SECRET=your_reddit_client_secret
PASSWORD=your_reddit_password
USER_AGENT=your_reddit_user_agent
USERNAME=your_reddit_username
DBUSER=your_database_username
DBPASSWORD=your_database_password
HOST=your_database_host
PORT=your_database_port
DB=your_database_name
```

3. Build and run the Docker containers using Docker Compose. If docker-compose is not installed, run **pip install docker-compose** first. The provided docker-compose.yml file defines the services for running the PostgreSQL database and the Python script container.
```
docker-compose up -d
```

## Usage
The Python script (scrape.py) extracts top posts from the "health" subreddit, performs NLP analysis on the titles, and stores the analyzed data in a PostgreSQL database.
```
python3 scrape.py
```

## Cron Job
The provided `crontab` file schedules the script to run daily at 8:30 PM. Adjust the timing in the crontab file as needed.

## Dependencies
- [praw](https://praw.readthedocs.io/en/stable/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- [spacy](https://spacy.io/)
- [scispacy](https://pypi.org/project/scispacy/)
- [PyDictionary](https://pypi.org/project/PyDictionary/)
- [psycopg2-binary](https://chat.openai.com/#:~:text=PyDictionary-,psycopg2%2Dbinary,-Docker%20Compose)

## Dashboard
View the output of my project [here](https://lookerstudio.google.com/reporting/00ad07d9-4231-4b82-9f08-0a8e04b7bcfb)!

<img width="1209" alt="Screenshot 2023-08-14 at 10 10 26 PM" src="https://github.com/jaclynfink/reddit-top-posts-rhealth/assets/36872212/49722a2c-12f5-4ca0-9015-62b47fa82638">

<img width="1064" alt="Screenshot 2023-08-14 at 10 10 40 PM" src="https://github.com/jaclynfink/reddit-top-posts-rhealth/assets/36872212/00e77c85-d5e4-4479-8bb1-64ea47331445">

<img width="1146" alt="Screenshot 2023-08-14 at 10 11 00 PM" src="https://github.com/jaclynfink/reddit-top-posts-rhealth/assets/36872212/b793a7e0-dc05-45f1-b9cf-069636233fbc">

<img width="1084" alt="Screenshot 2023-08-14 at 10 11 12 PM" src="https://github.com/jaclynfink/reddit-top-posts-rhealth/assets/36872212/499411d2-74ca-437a-ab92-2c3e42f4e270">

