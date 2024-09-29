import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
# Load data
df = pd.read_csv("https://raw.githubusercontent.com/hajee17/Submission_BelajarAnalisisDatadenganPython_AirQualityDataset/main/dashboard/main_data.csv")

# Convert 'date' column to datetime
df['date'] = pd.to_datetime(df['date'])

# Set page title and layout
st.set_page_config(page_title='Dashboard Kualitas Udara', layout='wide')

# Title
st.title('Dashboard Kualitas Udara di Beijing')

# Dropdown for station selection
selected_station = st.selectbox('Pilih Stasiun', df['station'].unique())

# Filter data for the selected station
filtered_df = df[df['station'] == selected_station]

# Create tabs
tab1, tab2, tab3 = st.tabs(["Tren Polusi", "Visualisasi Perbandingan", "Analisis Lanjutan"])

### Tab 1: Tren Polusi (Line Chart + Boxplot)
with tab1:
    st.subheader(f'Tren dan Distribusi Polusi di Stasiun {selected_station}')
    
    # Pollutants to visualize
    pollutants = ['PM2.5', 'PM10', 'SO2', 'NO2', 'TEMP']

    for pollutant in pollutants:
        # Line chart to show trends over time
        st.markdown(f"### Tren {pollutant}")
        fig_line = px.line(filtered_df, x=filtered_df['date'], y=pollutant, title=f'Tren {pollutant} di Stasiun {selected_station}')
        st.plotly_chart(fig_line)

        # Bar chart to show distribution
        st.markdown(f"### Distribusi {pollutant}")
        fig_bar = px.bar(filtered_df, x=filtered_df['date'].index, y=pollutant, title=f'Distribusi {pollutant} di Stasiun {selected_station}')
        st.plotly_chart(fig_bar)
        if pollutant == 'PM2.5':
            st.write("Tren PM2.5 menunjukkan fluktuasi kadar polutan selama periode waktu yang diamati. "
                     "Kenaikan kadar PM2.5 dapat terkait dengan aktivitas industri, lalu lintas, dan kondisi meteorologi.")
        elif pollutant == 'TEMP':
            st.write("Tren suhu menunjukkan pola fluktuasi yang dapat memengaruhi kualitas udara. "
                     "Suhu yang lebih tinggi dapat mempercepat reaksi kimia yang menghasilkan polutan.")
        elif pollutant == 'PM10':
            st.write("Tren PM10 menunjukkan variasi dalam kadar polutan. "
                     "Kadar PM10 yang tinggi sering kali berhubungan dengan cuaca kering dan angin.")
        elif pollutant == 'SO2':
            st.write("Tren SO2 menunjukkan konsentrasi gas yang dapat meningkat selama periode pembakaran bahan bakar fosil. "
                     "Kadar yang tinggi dapat menyebabkan masalah kesehatan, terutama pada populasi rentan.")
        elif pollutant == 'NO2':
            st.write("Tren NO2 menunjukkan perubahan konsentrasi yang berhubungan dengan lalu lintas kendaraan. "
                     "Kadar NO2 yang tinggi dapat memiliki dampak jangka panjang pada kesehatan masyarakat.")

### Tab 2: Visualisasi Perbandingan
with tab2:
    st.subheader('Visualisasi Perbandingan')

    # Scatter plot for TEMP vs PM2.5
    fig = px.scatter(filtered_df, x='TEMP', y='PM2.5', title='Scatter Plot TEMP vs PM2.5')
    st.plotly_chart(fig)

    # Boxplot comparison for PM2.5 across stations
    fig = px.box(df, x='station', y='PM2.5', title='Perbandingan PM2.5 Antar Stasiun')
    st.plotly_chart(fig)

    # Heatmap comparison of pollutants across stations
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

    # Bar plot comparison of mean pollutant levels across stations
    fig = px.bar(pollutants_mean, x='station', y=pollutants, barmode='group', title='Rata-rata Polutan di Setiap Stasiun')
    st.plotly_chart(fig)

### Tab 3: Analisis Lanjutan Geospatial Analysis & Clustering
with tab3:
    st.subheader('Analisis Lanjutan: Clustering')

    ## Clustering Analysis
    st.markdown("### Clustering of Stations Based on Pollutants")

    # Select pollutants for clustering
    pollutants_for_clustering = ['PM2.5', 'PM10', 'SO2', 'NO2']
    
    # Data preparation: scaling pollutants for clustering
    clustering_data = df.groupby('station')[pollutants_for_clustering].mean().dropna()
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(clustering_data)
    
    # K-means clustering
    kmeans = KMeans(n_clusters=3, random_state=42)
    clusters = kmeans.fit_predict(scaled_data)

    # Add cluster labels to dataframe
    clustering_data['Cluster'] = clusters
    clustering_data = clustering_data.reset_index()

    # Visualize clusters
    fig_clusters = px.scatter(clustering_data, x='PM2.5', y='PM10', color='Cluster',
                              hover_data=['station'], title='Clustering Stasiun Berdasarkan Polutan')
    st.plotly_chart(fig_clusters)
    
    # Display clustering result as a table
    st.write(clustering_data[['station', 'Cluster']])