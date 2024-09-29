import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
from datetime import datetime

# Load data
df = pd.read_csv('main_data.csv')

# Konversi kolom 'date' menjadi datetime
df['date'] = pd.to_datetime(df['date'])

# Hitung Recency, Frequency, dan Monetary untuk setiap stasiun
df['Recency'] = df.groupby('station')['date'].transform(lambda x: (x.max() - x).dt.days)
df['Frequency'] = df.groupby('station')['PM2.5'].transform('count')
df['Monetary'] = df.groupby('station')['PM2.5'].transform('mean')

# Set page title
st.set_page_config(page_title='Dashboard Kualitas Udara', layout='wide')

# Title
st.title('Dashboard Kualitas Udara di Beijing')

# Dropdown for station selection
selected_station = st.selectbox('Pilih Stasiun', df['station'].unique())

# Create tabs
tab1, tab2, tab3 = st.tabs(["Tren Polusi", "Visualisasi Perbandingan", "Analisis Lanjutan"])

with tab1:
    # PM2.5 graph
    st.subheader(f'Tren PM2.5 di Stasiun {selected_station}')
    filtered_df = df[df['station'] == selected_station]
    fig = px.line(filtered_df, x='date', y='PM2.5', title=f'Tren PM2.5 di Stasiun {selected_station}')
    st.plotly_chart(fig)

    # Temperature graph
    st.subheader(f'Tren Suhu di Stasiun {selected_station}')
    fig = px.line(filtered_df, x='date', y='TEMP', title=f'Tren Suhu di Stasiun {selected_station}')
    st.plotly_chart(fig)

    # PM10 graph
    st.subheader(f'Tren PM10 di Stasiun {selected_station}')
    fig = px.line(filtered_df, x='date', y='PM10', title=f'Tren PM10 di Stasiun {selected_station}')
    st.plotly_chart(fig)

    # SO2 graph
    st.subheader(f'Tren SO2 di Stasiun {selected_station}')
    fig = px.line(filtered_df, x='date', y='SO2', title=f'Tren SO2 di Stasiun {selected_station}')
    st.plotly_chart(fig)

    # NO2 graph
    st.subheader(f'Tren NO2 di Stasiun {selected_station}')
    fig = px.line(filtered_df, x='date', y='NO2', title=f'Tren NO2 di Stasiun {selected_station}')
    st.plotly_chart(fig)

with tab2:
    # TEMP vs PM2.5 scatter plot
    st.subheader('Scatter Plot TEMP vs PM2.5')
    fig = px.scatter(filtered_df, x='TEMP', y='PM2.5', title='Scatter Plot TEMP vs PM2.5')
    st.plotly_chart(fig)

    # PM2.5 boxplot
    st.subheader('Perbandingan PM2.5 Antar Stasiun')
    fig = px.box(df, x='station', y='PM2.5', title='Perbandingan PM2.5 Antar Stasiun')
    st.plotly_chart(fig)

    # PM2.5 distribution histogram
    st.subheader('Distribusi PM2.5')
    fig = px.histogram(filtered_df, x='PM2.5', nbins=30, title='Distribusi PM2.5')
    st.plotly_chart(fig)

    # PM10 vs PM2.5 scatter plot
    st.subheader('Scatter Plot PM10 vs PM2.5')
    fig = px.scatter(filtered_df, x='PM10', y='PM2.5', title='Scatter Plot PM10 vs PM2.5')
    st.plotly_chart(fig)

    # Heatmap comparing pollutants across stations
    st.subheader('Perbandingan Rata-rata Polutan Antar Stasiun')
    pollutants = ['PM2.5', 'PM10', 'SO2', 'NO2']
    pollutant_means = df.groupby('station')[pollutants].mean().reset_index()

    fig = go.Figure(data=go.Heatmap(
        z=pollutant_means[pollutants].values,
        x=pollutants,
        y=pollutant_means['station'],
        colorscale='YlOrRd'
    ))
    fig.update_layout(title='Rata-rata Polutan di Berbagai Stasiun', xaxis_title='Polutan', yaxis_title='Stasiun')
    st.plotly_chart(fig)

with tab3:
    st.subheader('Analisis Lanjutan: RFM Analysis')
    st.write("Recency, Frequency, and Monetary trends across stations.")
    
    # Recency Analysis
    rfm_fig = px.bar(df, x='station', y='Recency', title='Recency Analysis')
    st.plotly_chart(rfm_fig)

    # Frequency Analysis
    frequency_fig = px.bar(df, x='station', y='Frequency', title='Frequency Analysis')
    st.plotly_chart(frequency_fig)

    # Monetary Analysis
    monetary_fig = px.bar(df, x='station', y='Monetary', title='Monetary Analysis')
    st.plotly_chart(monetary_fig)
