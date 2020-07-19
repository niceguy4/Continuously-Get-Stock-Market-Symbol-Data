# Continuously-Get-Stock-Market-Symbol-Data
Script gathers stock market symbol data from yahoo finance and updates data over time

Description:
  This script can be setup to pull stock market symbol data over time using a scheduler program/script. For example, this script could do stock market symbol data updates every 7-days. The script will check if previous data exists in your script Market Data folder. If data exists it will update the existing file with the new data. If no file exists a new file is created.

  Variable stock_symbol_requests holds the symbol data and symbol names. The default symbols are index found on yahoo finance. They require the "^" character. If you want to search for Ford symbol F you do not need the "^" symbol.
  



Requirements:
  1. Create the following folders where your script runs, Data/Market Data/ and Data/Logs/
    a. If the script is in C:\MyFiles\ you need to create C:\MyFiles\Data\Market Data\ and C:\MyFiles\Data\Logs\
  2. Packages: datatime, time, yfinance, csv, os, random
    a. May need to add packages datatime and csv using 'pip' function
    b. You will need to install yfinance. This script pulls the stock market data
      I. https://pypi.org/project/yfinance/

Other Notes
  Simple Bot Detection Avoidance Tactics
    In the main while loop function, the script will randomly generate a wait timer based on 1-hour. The range is from 0 minutes to 60 minutes. This is to avoid any server side detection look for pulls that are done systematically, e.g. every 1-hour or 30-minutes. 
    There is a 7 second wait delay between data pull requests. This could be extended or shorten. Be careful removing this delay because you could risk getting throttled by the server, ip-ban or some other restrictions. 
    
  Ubuntu Crontabs Scheduler
   If you use crontabs scheduler you may need to edit the pathing data within the script from /Data/Market Data/ to home/YOUR USER NAME/Desktop/Data/Logs/
