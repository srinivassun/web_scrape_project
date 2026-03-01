from datetime import datetime
import time

import requests
import selectorlib

from send_email import send_email

URL = "http://programmer100.pythonanywhere.com/"
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
    now = datetime.now().strftime("%y-%m-%d-%H-%M-%S")
    with open("data_new.txt","a") as file:
        file.write(f"{now},{extract}\n")

def read_extract():
    with open("data_new.txt","r") as file:
        return file.read()


def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract_temperature.yaml")
    return extractor.extract(source)["temperature"]

while True:
    scraped = scrape(URL)
    extracted = extract(scraped)
    print(extracted)
    store_extract(extracted)
    #send_out_email(extracted)
    time.sleep(2)