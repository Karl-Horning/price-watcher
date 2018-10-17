import time
from pw_functions import get_price_from_amazon, write_to_csv_file, write_to_txt_file

if __name__ == '__main__':
    # runs every hour for a month
    total_days = 30
    day_number = 1

    while day_number <= total_days:
        time.sleep(3600)
        smp = get_price_from_amazon('https://www.amazon.co.uk/Super-Mario-Party-Nintendo-Switch/dp/B07DTNGK5V/ref=sr_1_3?s=videogames&ie=UTF8&qid=1539340023&sr=1-3', 42.99)
        write_to_csv_file('log', [smp['current_date'], smp['current_time'], smp['title'], smp['price']])
        print(f'{smp} added to CSV file')