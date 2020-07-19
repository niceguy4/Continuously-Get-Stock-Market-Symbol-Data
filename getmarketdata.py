import datetime
import time
import yfinance as yf
import csv
import os
import random


#   stock symbol : stock name
stock_symbol_requests = {'^GSPC': 'SP500', '^DJI': 'DOW', '^IXIC': 'NASDAQ'}
start_date_no_file = '2020-06-19'


def date_post():
    return datetime.datetime.today().strftime('%Y%m%d')


def time_post():
    return datetime.datetime.today().strftime('%Y%m%d %H-%M-%S')


#   get last market data update date and count days since today and update
def get_market_data_start_date(stocksymbol):
    today = datetime.date.today()

    count_days = 0

    #   files are missing. restart the full data pulls
    if not (os.path.isfile('Data/Market Data/' + str(stocksymbol[1]) + '.csv')):
        today = start_date_no_file
        count_days = 5
        file_exists = False
        return today, count_days, file_exists
    else:
        f_start_date = open('Data/Market Data/' + str(stocksymbol[1]) + '.csv', newline='', encoding='utf-8')
        mdreader = csv.reader(f_start_date, skipinitialspace=True)

        f_start_date.seek(0)
        mdreader = list(mdreader)

        #   function removes accidental white space on csv pull
        row_count = 0
        del_list = []
        for get_print_lines in mdreader:
            if get_print_lines:
                row_count = row_count + 1
            if not get_print_lines:
                del_list.append(row_count)
        row_count = 0
        for del_spaces in del_list:
            del mdreader[del_spaces]

        row_count = sum(1 for row in mdreader)
        print(row_count)

        f_start_date.seek(0)

        print(mdreader[row_count - 1])
        last_row_date = mdreader[row_count - 1]
        date_last = last_row_date[0]
        f_start_date.close()
        file_exists = True

        if str(date_last) == str(today):
            print("today is the day")
            print(today)
            return today, count_days, file_exists
        else:
            while str(date_last) != str((today - datetime.timedelta(days=count_days))):
                count_days = count_days + 1
            print(str((today - datetime.timedelta(days=count_days - 1))))
            return str((today - datetime.timedelta(days=count_days - 1))), count_days, file_exists
    return today, count_days, file_exists


#   write to temp file so main file is not over written
def stock_data_to_csv(file_exists, stocksymbol, md_start_date, end_date_grab_data):

    # get data on this ticker
    tickerData = yf.Ticker(stocksymbol[0])

    # get the historical prices for this ticker
    tickerDf = tickerData.history(period='1d', start=md_start_date, end=end_date_grab_data)

    # see your data
    print(tickerDf)
    if file_exists:
        tickerDf.to_csv('Data/Market Data/' + str(stocksymbol[1]) + '_temp.csv')

    if not file_exists:
        tickerDf.to_csv('Data/Market Data/' + str(stocksymbol[1]) + '.csv')
    return


#   append main file and delete temp file
def append_stock_data(stocksymbol):

    f_reader = open('Data/Market Data/' + str(stocksymbol[1]) + '_temp.csv', newline='', encoding='utf-8')
    mdreader = csv.reader(f_reader)
    row_count = sum(1 for row in mdreader)
    f_reader.seek(0)
    if row_count > 1:
        print(row_count)
        mdreader = list(mdreader)
        mdreader.pop(0)
        f_write = open('Data/Market Data/' + str(stocksymbol[1]) + '.csv', 'a+', newline='', encoding='utf-8')
        market_data_write = csv.writer(f_write, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        market_data_write.writerows(mdreader)
        f_write.close()
    f_reader.close()
    os.remove("Data/Market Data/" + str(stocksymbol[1]) + "_temp.csv")

    return


while True:
    try:
        last_count_days = 0
        end_date_grab_data = datetime.date.today()

        #   check if last update is > 4 days old
        #   prevents update issues with yfinance
        #   get last market data update date
        for get_data in stock_symbol_requests.items():
            file_date, last_count_days, file_exists = get_market_data_start_date(get_data)

        #   random wait to disguise bot pulls (1-hour window)
        rand_wait_seconds = int(random.random()*3600)
        print("Random minutes - waiting: " + str(int(rand_wait_seconds/60)))
        time.sleep(rand_wait_seconds)

        #   > 4 days. pull new market data using today and last update date
        #   append to csv file. was unable to figure out how csv is written on yfinance
        #   so it is written to temp file then appended
        if last_count_days > 4:
            for get_data in stock_symbol_requests.items():
                stock_data_to_csv(file_exists, get_data, file_date, end_date_grab_data)
                time.sleep(7)
            if file_exists:
                for get_data in stock_symbol_requests.items():
                    append_stock_data(get_data)
            print("Market data update complete.")
            exit()
        else:
            print("Last market update less than 4 days old.")
        exit()

        #   handle any errors and write to file for tracking
    except Exception as message_error:
        exception_error_time = time_post()
        print("Exception Market Data Script")
        f = open("Data/Logs/Error Logs.txt", "a", encoding="utf-8")
        f.write("Exception Market Data Script: " + str(exception_error_time) + "\nError Message: " + str(message_error) + "\n")
        f.close()
        time.sleep(240)
