import time

import requests
import selectorlib

from send_email import send_email

URL = "http://programmer100.pythonanywhere.com/tours/"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

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
        content = read_extract()
        if extracted not in content:
            store_extract(extracted)
            send_out_email(extracted)
    time.sleep(2)