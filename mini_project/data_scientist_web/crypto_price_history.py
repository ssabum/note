import streamlit as st
from cryptocmd import CmcScraper
import plotly.express as px

# 제먹 출력
st.write('# 비트코인 BTC 데이터')

# https://coinmarketcap.com
# 날짜 순서 주의
scraper = CmcScraper('BTC', '01-01-2021', '30-01-2021')

df = scraper.get_dataframe()

# 차트를 이쁘게 작성
fig_close = px.line(df, x='Date', y=['Open', 'High', 'Low', 'Close'], title='가격')
fig_volume = px.line(df, x='Date', y=['Volume'], title='거래량')

# 차트 출력
st.plotly_chart(fig_close)
st.plotly_chart(fig_volume)