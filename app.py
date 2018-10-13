import csv
import datetime
import urllib3
import requests
from bs4 import BeautifulSoup

def get_price_from_amazon(url, best_price):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    now = datetime.datetime.now()
    current_date_time = now.strftime("%Y-%m-%d %H:%M:%S")

    # Search the returned HTML for the title and the price
    title = soup.find(id='productTitle').string
    price = soup.find(id='priceblock_ourprice').string
    # Remove the whitespace from the beginning and end of the title
    title = title.strip()
    # Remove the pound sign and convert the price from a string to a decimal
    price = float(
        price.replace('£', '')
    )

    # Write the price to a text file
    f = open("log.txt", "w")
    f.write(f'{title}: £{price}')

    # Append the price to a CSV file
    with open("log.csv", "a") as price_file:
        price_writer = csv.writer(price_file, delimiter=',')
        price_writer.writerow([current_date_time, title, price])

    # Decide whether or not to send the email
    # if price == best_price:
    #     print('Same price')
    # elif price < best_price:
    #     print('Send email')
    # else:
    #     print('It\'s more expensive!')

    return f'{title}: £{price}'

if __name__ == '__main__':
    print(get_price_from_amazon('https://www.amazon.co.uk/Super-Mario-Party-Nintendo-Switch/dp/B07DTNGK5V/ref=sr_1_3?s=videogames&ie=UTF8&qid=1539340023&sr=1-3', 42.99))
    print(get_price_from_amazon('https://www.amazon.co.uk/Nintendo-Switch-Joy-Controller-Pair/dp/B01NBU1LP4/ref=pd_rhf_ee_s_cp_0_2?_encoding=UTF8&pd_rd_i=B01NBU1LP4&pd_rd_r=6XN8MG93RXAEB4BNXY1Z&pd_rd_w=AyJLg&pd_rd_wg=ibQZJ&psc=1&refRID=6XN8MG93RXAEB4BNXY1Z', 42.99))