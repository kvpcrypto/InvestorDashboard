#import required libraries
import streamlit as st
import yfinance as yf
from datetime import datetime

# #ticker search feature in sidebar
# st.sidebar.subheader("""Stock Search Web App""")
# selected_stock = st.sidebar.text_input("Enter a valid stock ticker...", "GOOG")
# button_clicked = st.sidebar.button("GO")
# if button_clicked == "GO":
#     main()


#main function
st.write("# Amazon")
st.subheader("""Daily **closing price** for """ + "TLSA")
#get data on searched ticker
stock_data = yf.Ticker("AMZN")
#get historical data for searched ticker
stock_df = stock_data.history(period='1d', start='2020-01-01', end=None)
#print line chart with daily closing prices for searched ticker
st.line_chart(stock_df.Close)

st.subheader("""Last **closing price** for """ + "AMZN")
#define variable today 
today = datetime.today().strftime('%Y-%m-%d')
#get current date data for searched ticker
stock_lastprice = stock_data.history(period='1d', start=today, end=today)
#get current date closing price for searched ticker
last_price = (stock_lastprice.Close)
#if market is closed on current date print that there is no data available
if last_price.empty == True:
    st.write("No data available at the moment")
else:
    st.write(last_price)

#get daily volume for searched ticker
st.subheader("""Daily **volume** for """ + "AMZN")
st.line_chart(stock_df.Volume)

#additional information feature in sidebar
st.sidebar.subheader("""Display Additional Information""")
#checkbox to display stock actions for the searched ticker
actions = st.sidebar.checkbox("Stock Actions")
if actions:
    st.subheader("""Stock **actions** for """ + "AMZN")
    display_action = (stock_data.actions)
    if display_action.empty == True:
        st.write("No data available at the moment")
    else:
        st.write(display_action)

#checkbox to display quarterly financials for the searched ticker
financials = st.sidebar.checkbox("Quarterly Financials")
if financials:
    st.subheader("""**Quarterly financials** for """ + "AMZN")
    display_financials = (stock_data.quarterly_financials)
    if display_financials.empty == True:
        st.write("No data available at the moment")
    else:
        st.write(display_financials)

#checkbox to display list of institutional shareholders for searched ticker
major_shareholders = st.sidebar.checkbox("Institutional Shareholders")
if major_shareholders:
    st.subheader("""**Institutional investors** for """ + "AMZN")
    display_shareholders = (stock_data.institutional_holders)
    if display_shareholders.empty == True:
        st.write("No data available at the moment")
    else:
        st.write(display_shareholders)

#checkbox to display quarterly balance sheet for searched ticker
balance_sheet = st.sidebar.checkbox("Quarterly Balance Sheet")
if balance_sheet:
    st.subheader("""**Quarterly balance sheet** for """ + "AMZN")
    display_balancesheet = (stock_data.quarterly_balance_sheet)
    if display_balancesheet.empty == True:
        st.write("No data available at the moment")
    else:
        st.write(display_balancesheet)

#checkbox to display quarterly cashflow for searched ticker
cashflow = st.sidebar.checkbox("Quarterly Cashflow")
if cashflow:
    st.subheader("""**Quarterly cashflow** for """ + "AMZN")
    display_cashflow = (stock_data.quarterly_cashflow)
    if display_cashflow.empty == True:
        st.write("No data available at the moment")
    else:
        st.write(display_cashflow)

#checkbox to display quarterly earnings for searched ticker
earnings = st.sidebar.checkbox("Quarterly Earnings")
if earnings:
    st.subheader("""**Quarterly earnings** for """ + "AMZN")
    display_earnings = (stock_data.quarterly_earnings)
    if display_earnings.empty == True:
        st.write("No data available at the moment")
    else:
        st.write(display_earnings)

#checkbox to display list of analysts recommendation for searched ticker
analyst_recommendation = st.sidebar.checkbox("Analysts Recommendation")
if analyst_recommendation:
    st.subheader("""**Analysts recommendation** for """ + "AMZN")
    display_analyst_rec = (stock_data.recommendations)
    if display_analyst_rec.empty == True:
        st.write("No data available at the moment")
    else:
        st.write(display_analyst_rec)