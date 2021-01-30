import streamlit as st
from cryptocmd import CmcScraper
import plotly.express as px
from datetime import datetime

st.write('# Cryptocurrency Web App')

# 사이드바를 만들어 사용자가 입력한 자료를 볼 수 있도록 설정
st.sidebar.header('Menu')
# 종목이름 설정
name = st.sidebar.selectbox('Name', ['BTC', 'ETH', 'USDT'])
# 시작과 끝 날짜 설정
start_date = st.sidebar.date_input('Start date', datetime(2021, 1, 1))
end_date = st.sidebar.date_input('End date', datetime(2021, 1, 30))

# https://coinmarketcap.com
# date type을 str type으로 변환
scraper = CmcScraper(name, start_date.strftime('%d-%m-%Y'), end_date.strftime('%d-%m-%Y'))
df = scraper.get_dataframe()

# 차트를 이쁘게 수정
fig_close = px.line(df, x='Date', y=['Open', 'High', 'Low', 'Close'], title='Price')
fig_volume = px.line(df, x='Date', y=['Volume'], title='Volume')

# 차트 출력
st.plotly_chart(fig_close)
st.plotly_chart(fig_volume)