import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from pandas_datareader import data as pdr
%matplotlib inline

from cryptocmd import CmcScraper
def get_coinmarketcap_data(symbol,start_date,end_date):
    # initialise scraper with time interval
    #scraper = CmcScraper("BNB", "01-01-2017", "27-01-2022")
    scraper = CmcScraper(symbol, start_date,end_date)
    # get raw data as list of list
    headers, data = scraper.get_data()
    # get data in a json format
    json_data = scraper.get_data("json")
    # export the data to csv
    scraper.export("csv")
    # get dataframe for the data
    df = scraper.get_dataframe()
    df['Date'] = pd.to_datetime(df['Date']).dt.date #Convert all date time fields to Date so that all date 
    df['Date'] = pd.to_datetime(df['Date']) #Now convert back to date
    df.set_index('Date', inplace=True)
    return df
	
from datetime import date
ticker_list=['BTC','ETH','BNB','XRP']
list_blkch_dataframes = []
#start_date= "01-01-2017"
#end_date="27-01-2022"
start_date= "1-1-2016"
end_date = date.today().strftime("%d-%m-%Y")
df_BTC=get_coinmarketcap_data("BTC",start_date,end_date)
df_ETH=get_coinmarketcap_data("ETH",start_date,end_date)
df_BNB=get_coinmarketcap_data("BNB",start_date,end_date)
df_XRP=get_coinmarketcap_data("XRP",start_date,end_date)
%store df_BTC
%store df_ETH
%store df_BNB
%store df_XRP
