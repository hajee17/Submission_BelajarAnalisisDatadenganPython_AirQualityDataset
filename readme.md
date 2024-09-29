# Proyek Analisis Data Kualitas Udara di Beijing

Proyek ini bertujuan untuk menganalisis data kualitas udara di Beijing dari tahun 2013-2017. Data yang digunakan adalah data kualitas udara yang dikumpulkan oleh stasiun pemantauan kualitas udara di Beijing. dan menyelesaikan tugas.

## Insight Tahapan yang dipakai dalam proyek ini
* 1. Gathering Data
     Insight: Data kualitas udara yang dikumpulkan dari berbagai stasiun mencakup parameter penting seperti PM2.5, PM10, SO2, NO2, dan suhu (TEMP). Ketersediaan data historis yang cukup memungkinkan analisis tren dan pola.
* 2. Data Cleaning
     Insight: Proses pembersihan data mengidentifikasi dan mengatasi nilai yang hilang, duplikasi, dan kesalahan format. Data yang bersih memastikan analisis yang lebih akurat dan terpercaya.
* 3. Data Exploration
     Insight: Analisis eksploratif awal menunjukkan distribusi parameter polusi udara, serta identifikasi stasiun dengan kualitas udara terbaik dan terburuk. Memahami distribusi dan nilai ekstrem membantu dalam menentukan fokus analisis lebih lanjut.
* 4. Descriptive Statistics
     Insight: Statistik deskriptif memberikan gambaran umum tentang data, termasuk rata-rata, median, dan varians dari setiap parameter. Ini membantu memahami variabilitas dan sifat data.
* 5. Trend Analysis
     Insight: Analisis tren mengungkapkan pola musiman dan fluktuasi waktu dalam data polusi. Misalnya, peningkatan PM2.5 selama periode tertentu dapat menunjukkan pengaruh faktor eksternal seperti cuaca atau aktivitas industri.
* 6. Comparative Analysis
     Insight: Perbandingan antar stasiun mengungkapkan perbedaan signifikan dalam kualitas udara. Ini membantu mengidentifikasi lokasi dengan polusi lebih tinggi dan menginformasikan kebijakan mitigasi.
* 7. Correlation Analysis
     Insight: Analisis korelasi antara berbagai parameter polusi memberikan wawasan tentang hubungan antara polutan. Misalnya, hubungan antara suhu dan konsentrasi PM2.5 dapat menunjukkan efek iklim terhadap polusi udara.
* 8. Advanced Analysis (RFM)
     Insight: Analisis RFM (Recency, Frequency, Monetary) memungkinkan pemahaman lebih dalam tentang pola polusi. Recency mengindikasikan seberapa baru data, Frequency menunjukkan frekuensi pengukuran, dan Monetary menggambarkan nilai rata-rata polutan. Ini membantu mengidentifikasi station yang perlu perhatian lebih.
* 9. Explanatory Analysis
     Insight: Analisis yang bersifat eksplanatori menghubungkan semua temuan dan menjelaskan pengaruh lingkungan, kebijakan, atau faktor lain terhadap kualitas udara. 

# Rangkuman Umum:
Proyek ini menghasilkan wawasan penting tentang kualitas udara di Beijing, dengan penekanan pada identifikasi pola polusi, analisis perbandingan antar stasiun, serta dampak dari berbagai faktor lingkungan. Hasil analisis ini dapat digunakan untuk menginformasikan kebijakan publik dan meningkatkan kesadaran masyarakat tentang masalah polusi udara.

## Struktur Proyek

* `data/`: direktori untuk menyimpan dataset kualitas udara di Beijing degan format .csv
* `notebooks.ipynb`: file notebook analisis data
* `dashboard/`: direktori untuk menyimpan kode dashboard
* `README.md`: file README untuk proyek ini



## Cara Menjalankan Proyek

1. Clone repository ini ke komputer Anda.
2. Install library yang dibutuhkan dengan menjalankan `pip install -r requirements.txt`.
3. Jalankan notebook analisis data dengan menjalankan `jupyter notebook` di direktori `notebooks/`.
4. Jalankan dashboard dengan menjalankan `python dashboard.py` di direktori `dashboard/`.

## Hasil Analisis

Hasil analisis data kualitas udara di Beijing dapat dilihat di dashboard yang dihasilkan oleh proyek ini. Dashboard ini menampilkan tren kualitas udara (PM2.5) di berbagai stasiun dari tahun 2013-2017, serta perbandingan tingkat polusi (PM2.5, PM10, SO2, NO2) antar stasiun.