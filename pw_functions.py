import csv
import datetime
import urllib3
import requests
from bs4 import BeautifulSoup

def get_price_from_amazon(url, best_price):
    result = dict()
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    now = datetime.datetime.now()
    result['current_date'] = now.strftime("%Y-%m-%d")
    result['current_time'] = now.strftime("%H:%M:%S")

    # Search the returned HTML for the title and the price
    title = soup.find(id='productTitle').string
    price = soup.find(id='priceblock_ourprice').string
    # Remove the whitespace from the beginning and end of the title
    result['title'] = title.strip()
    # Remove the pound sign and convert the price from a string to a decimal
    result['price'] = float(
        price.replace('£', '')
    )

    return result

def write_to_csv_file(file_name, data):
    # Append the price to a CSV file
    with open(f'{file_name}.csv', 'a') as price_file:
        price_writer = csv.writer(price_file, delimiter=',')
        price_writer.writerow(data)
    return f'{data} written to {file_name}.csv'

def write_to_txt_file(file_name, data):
    # Write the price to a text file
    f = open(f'{file_name}.txt', 'w')
    f.write(
        str(data)
        )
    return f'{data} written to {file_name}.txt'