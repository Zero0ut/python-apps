import pandas as pandas
import numpy as numpy
import yfinance as yf
import datetime as dt
from pandas_datareader import data as pdr

yf.pdr_override()

stock=input("Enter a stock ticker symbol: ")
print(stock)

startyear=2019
startmonth=1
startday=1

start=dt.datetime(startyear,startmonth,startday)

now=dt.datetime.now()

df=pdr.get_data_yahoo(stock,start,now)
print(df)

ma=50
smaString="Sma_"+str(ma)

df[smaString]=df.iloc[:,4].rolling(window=ma).mean()
print(df)

df=df.iloc[ma:]
print(df)

#Access data from AdjustedClose and sma
#for i in df.index:
#	print("Adjusted Close: " + str(df["Adj Close"][1]))
#	print(smaString + ": " + str(df[smaString][1]))

numH=0
numC=0

for i in df.index:
	if(df["Adj Close"][i]>df[smaString][i]):
		print("The Close is higher")
		numH+=1
	else:
		print("The Close is lower")
		numC+=1

print(str(numH))
print(str(numC))


