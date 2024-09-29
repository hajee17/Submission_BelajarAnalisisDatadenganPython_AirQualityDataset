import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go

# Load \
df = pd.read_csv("https://raw.githubusercontent.com/hajee17/Submission_BelajarAnalisisDatadenganPython_AirQualityDataset/main/dashboard/main_data.csv")
# Konversi kolom 'date' menjadi datetime
df['date'] = pd.to_datetime(df['date'])

# Set page title
st.set_page_config(page_title='Dashboard Kualitas Udara', layout='wide')

# Title
st.title('Dashboard Kualitas Udara di Beijing')

# Dropdown for station selection
selected_station = st.selectbox('Pilih Stasiun', df['station'].unique())

# Filter data for the selected station
filtered_df = df[df['station'] == selected_station]

# Create tabs
tab1, tab2, tab3 = st.tabs(["Tren Polusi", "Visualisasi Perbandingan", "Analisis Lanjutan"])

with tab1:
    st.subheader(f'Tren Polusi di Stasiun {selected_station}')
    pollutants = ['PM2.5', 'TEMP', 'PM10', 'SO2', 'NO2']
    
    for pollutant in pollutants:
        fig = px.line(filtered_df, x='date', y=pollutant, title=f'Tren {pollutant} di Stasiun {selected_station}')
        st.plotly_chart(fig)

with tab2:
    st.subheader('Visualisasi Perbandingan')
    
    # TEMP vs PM2.5 scatter plot
    fig = px.scatter(filtered_df, x='TEMP', y='PM2.5', title='Scatter Plot TEMP vs PM2.5')
    st.plotly_chart(fig)

    # PM2.5 boxplot
    fig = px.box(df, x='station', y='PM2.5', title='Perbandingan PM2.5 Antar Stasiun')
    st.plotly_chart(fig)

    # Heatmap comparing pollutants across stations
    st.subheader('Perbandingan Rata-rata Polutan Antar Stasiun')
    pollutants_mean = df.groupby('station')[pollutants].mean().reset_index()
    fig = go.Figure(data=go.Heatmap(
        z=pollutants_mean[pollutants].values,
        x=pollutants,
        y=pollutants_mean['station'],
        colorscale='YlOrRd'
    ))
    fig.update_layout(title='Rata-rata Polutan di Berbagai Stasiun', xaxis_title='Polutan', yaxis_title='Stasiun')
    st.plotly_chart(fig)

with tab3:
    st.subheader('Analisis Lanjutan: RFM Analysis')
    
    # Hitung RFM hanya untuk stasiun yang dipilih
    rfm_data = filtered_df.agg(
        Recency=('date', lambda x: (pd.to_datetime('now') - x.max()).days),
        Frequency=('date', 'count'),
        Monetary=('PM2.5', 'mean')
    ).reset_index()
    
    # Tampilkan tabel RFM
    st.write(rfm_data)

    # Visualisasi RFM
    st.bar_chart(rfm_data.set_index('station'))
