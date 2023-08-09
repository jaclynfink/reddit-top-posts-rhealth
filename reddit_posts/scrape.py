import praw
from dotenv import load_dotenv
import os
import spacy
import datetime
from PyDictionary import PyDictionary
import psycopg2

load_dotenv(dotenv_path='credentials.env', verbose=True)

# Extract data using Reddit API
reddit = praw.Reddit(
    client_id=os.getenv("CLIENT_ID"),
    client_secret=os.getenv("CLIENT_SECRET"),
    password=os.getenv("PASSWORD"),
    user_agent=os.getenv("USER_AGENT"),
    username=os.getenv("USERNAME"),
)

# Connect to Postgres database
connection = psycopg2.connect(user=os.getenv("DBUSER"),
                                  password=os.getenv("DBPASSWORD"),
                                  host=os.getenv("HOST"),
                                  port=os.getenv("PORT"),
                                  database=os.getenv("DB"))

cursor = connection.cursor()


current_datetime = datetime.datetime.now()
dictionary = PyDictionary()

top_15_title_list = []
top_15_url_list = []
for submission in reddit.subreddit("health").top(time_filter='day', limit=15):
    top_15_title_list.append(submission.title)
    top_15_url_list.append('http://www.reddit.com'+ submission.permalink)


# scispaCy for science/medical nlp
nlp = spacy.load('en_core_sci_md')

for x in range(0, len(top_15_title_list)):
    doc = nlp(top_15_title_list[x])
    for y in range(0, len(list(doc.ents))):
        word = str(doc.ents[y]).lower()
        url = top_15_url_list[x]
        try:
            definition = str(dictionary.meaning(str(word)))
        except:
            definition = str('')
        #Load into Postgresql
        postgres_insert_query = """ INSERT INTO top_posts (date_time, word, url, definition) VALUES (%s,%s,%s,%s)"""
        record_to_insert = (current_datetime, word, url, definition)
        cursor.execute(postgres_insert_query, record_to_insert)

        connection.commit()
        count = cursor.rowcount
        print(count, "Record inserted successfully into top_posts table")  