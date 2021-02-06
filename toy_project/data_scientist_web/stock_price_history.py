# streamlit사용
import streamlit as st
# 주식데이터 읽어오기
import pandas_datareader as pdr

# 마크다운으로 제목 설정
st.write('''
# 삼성전자 주식 데이터
마감 가격과 거래량을 차트로 보여줍니다!
''')

# https://finance.yahoo.com/quote/005930.KS?p=005930.KS
df = pdr.get_data_yahoo('005930.KS', '2020-01-01', '2021-01-30')

# 차트 출력
st.line_chart(df.Close)
st.line_chart(df.Volume)