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

nba_stats_df = nba_stats_df[nba_stats_df['PTS'] >= 15]
nba_stats_df = nba_stats_df[nba_stats_df['G'] >= 60]

columns_to_keep = ['Player', 'Pos', 'Age', 'Tm', 'G', 'FG%', 'TRB', 'AST', 'PTS', 'STL', 'BLK']
nba_stats_df = nba_stats_df[columns_to_keep]

nba_stats_df['Player'] = nba_stats_df['Player'].str.replace('?', 'c')

st.header('Exploring NBA Player Stats')

show_advanced_stats = st.checkbox('Show Advanced Stats')

if show_advanced_stats:
    fig_hist = px.histogram(nba_stats_df, x='PTS', title='Points per Game Distribution')
    st.plotly_chart(fig_hist)

    fig_scatter = px.scatter(nba_stats_df, x='AST', y='TRB', color='Pos', hover_name='Player', title='Assists vs. Rebounds')
    st.plotly_chart(fig_scatter)
else:
    st.write("Check the box to show advanced stats.")
