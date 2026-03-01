import time

import requests
import selectorlib
import sqlite3

from send_email import send_email

URL = "http://programmer100.pythonanywhere.com/tours/"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
#Establish a connection and cursor
connection = sqlite3.Connection("data.db")
cursor = connection.cursor()

def scrape(url):
    response = requests.get(url, headers=HEADERS)
    source = response.text
    return source

def send_out_email(message):
    print("Email was Sent")
    send_email(message)


def store_extract(extract):
    with open("data.txt","a") as file:
        file.write(extract + "\n")

def store_in_database(extract):
    print("Inserting data in database")
    events = str(extract)
    rows = events.split(",")
    print(rows)
    new_rows = [tuple(rows)]
    cursor.executemany("insert into events values(?,?,?)", new_rows)
    connection.commit()

def read_extract():
    with open("data.txt","r") as file:
        return file.read()


def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    return extractor.extract(source)["tours"]

while True:
    scraped = scrape(URL)
    extracted = extract(scraped)
    print(extracted)
    if extracted != 'No upcoming tours':
        store_in_database(extracted)
    time.sleep(2)