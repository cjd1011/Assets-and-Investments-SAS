# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import yfinance as yf
import streamlit as st
import pandas as pd

from PIL import Image

#img = "C:\Users\camilo.diaz.carvajal\Documents\CAMILO\A&I LOGO CARTA2.PNG)"
#Image(url=img)

st.write("""
# Assets & Investments S.A.S Price App
Shown are the stock closing price and volume of Bancolombia (CIB)!
""")

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol
tickerSymbol = 'CIB'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2021-1-19')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
st.line_chart(tickerDf.Dividends)

#get recommendation data for ticker
tickerData.recommendations
tickerData.balance_sheet
tickerData.balancesheet
tickerData.financials
st.write("""
         ***Relevant information***
         """)
#tickerData.info
st.write("""
         Institutional Holders
         """)
tickerData.institutional_holders
st.write("""
         Mutual Fund Holders
         """)

tickerData.mutualfund_holders



