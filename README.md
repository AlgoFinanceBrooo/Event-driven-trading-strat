# Event-driven-trading-strat
FOREX Event-driven trading strategy. Backtesting with HF tick-data.

Data source:

US-economic calendar: 
From financial model prep (FMP) API, provided for free after registration. Alternatively, free NASDAQ datalink API can provide the same data but in a different original format.

tick-data:
From Darwinex DB. Download FileZilla.exe to view and download each load of data from DWX database through its FTP server:

Username + Password: Provide after registration for live-trading account with DWX
FTPS server:	ftp://tickdata.darwinex.com
Port:	21

Save multiple gzip files in one folder and use the tick-merger notebook to merge data into separate years. Afterward, save as file.csv.


Share link to EURUSD tick-data. This is a large file, best we do it together and find a share folder.

https://1drv.ms/f/s!AqQFdRBGgexSzVhFYW4npJqcrq_t?e=Wpj28B
