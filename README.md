# Continuously-Get-Stock-Market-Symbol-Data
Script uses [yfinance](https://pypi.org/project/yfinance/) to gather stock market symbol data from yahoo finance and updates data over time.

## Description:

This script can be setup to pull stock market symbol data over time using a scheduler program/script or used for single one-time pull data requests. For example, this script could pull stock market symbol data updates every 7-days. The script will check if previous data exists in your script Market Data folder. If data exists, it will update the existing file with the new data. If no file exists, a new file is created. The script uses yfinance to pull data from Yahoo Finance's Historical Data page (Ford [example](https://finance.yahoo.com/quote/F/history?p=F)).

### Prerequisites:

1. Create the following folders where your script runs, Data/Market Data/ and Data/Logs/. If the script is in C:\MyFiles\ you need to create C:\MyFiles\Data\Market Data\ and C:\MyFiles\Data\Logs\
    
2. Packages: datatime, time, yfinance, csv, os, random. You may need to add packages datatime and csv using 'pip' function. You will need to install yfinance. This script pulls the stock market data. Install via 'pip' or instructions can be found here: https://pypi.org/project/yfinance/

##### Stock Market Ticker Data

The variable **stock_symbol_requests** holds the ticker symbol and stock position names. The default ticker symbols are index funds (S&P500, DOW, NASDAQ) found on yahoo finance. Index symbols require the "^" character. If you want to search for stocks, mutuals or etfs, use the actual ticker symbol. For example, to search Ford use the ticker symbol F. You do not need the "^" symbol. 

#### Delete File Command

Full disclosure. This script uses a command to delete the temporary file that is created by the pull data request. This is found at the end of the **def append_stock_data()** function.

#### Simple Bot Detection Avoidance Tactics

In the main while loop function, the script will randomly generate a wait timer based on 1-hour. The range is from 0 to 60 minutes. This is to reduce the probability that Yahoo's website detects the scripts pull requests. Continuously making pull requests from Yahoo Finance's website every 30-seconds or systematically, e.g. every 1-hour or 30-minutes could be recognized by Yahoo and stopped. This feature is optional and can be removed from the script.

There is a 7 second wait delay between ticker symbol pull requests. This delay could be extended or shortened. Be careful removing this delay, because you could risk getting throttled by the server, ip-ban or experience some other restrictions.
    
#### Ubuntu Crontabs Scheduler

If you use crontabs scheduler you may need to edit the pathing data within this python script from /Data/Market Data/ to home/YOURUSERNAME/Desktop/Data/Logs/

#### yfinance

The script documentation can be found on the author's website: https://pypi.org/project/yfinance/ .
  
