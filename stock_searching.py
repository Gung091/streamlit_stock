# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YIPg_NutY939IpjhqHKpdjsH9qiGJDfH
"""

import pandas as pd
import streamlit as st

TAI_ind = 'https://isin.twse.com.tw/isin/C_public.jsp?strMode=2'
df = pd.read_html(TAI_ind, encoding='cp950')

df_split = df[0][0][2:].str.split(expand=True)

df_split = df_split.apply(lambda x: x.str.split('\u3000').str[0:2].str.join(' '), axis=1)

df_split[0] = df_split[0].apply(lambda x: x+'.TW')

st.title('台灣股票代號查詢')
query_type = st.radio('查詢方式', ['代號查名稱', '名稱查代號'])

if query_type == '代號查名稱':
    search_code = st.text_input('請輸入代號')
    search_result = df_split[df_split[0] == search_code.upper()]
else:
    search_name = st.text_input('請輸入名稱')
    search_result = df_split[df_split[1].str.contains(search_name)]