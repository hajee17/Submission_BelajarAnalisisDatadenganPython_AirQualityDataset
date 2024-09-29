# Proyek Analisis Data Kualitas Udara di Beijing

Proyek ini bertujuan untuk menganalisis data kualitas udara di Beijing dari tahun 2013-2017. Data yang digunakan adalah data kualitas udara yang dikumpulkan oleh stasiun pemantauan kualitas udara di Beijing. dan menyelesaikan tugas.

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