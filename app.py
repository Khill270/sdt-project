import streamlit as st
import pandas as pd
import plotly.express as px

filename = '23-24 NBA Player Stats - Regular.csv'
encoding = 'latin-1'

try:
    nba_stats_df = pd.read_csv(filename, encoding=encoding, delimiter=';')
    print(nba_stats_df.head(10))
except UnicodeDecodeError as e:
    print(f"UnicodeDecodeError: {e}")

st.header('Exploring NBA Player Stats')

fig_hist = px.histogram(df, x='PTS', title='Points per Game Distribution')
st.plotly_chart(fig_hist)
fig_scatter = px.scatter(df, x='AST', y='TRB', color='Pos', hover_name='Player', title='Assists vs. Rebounds')
st.plotly_chart(fig_scatter)
