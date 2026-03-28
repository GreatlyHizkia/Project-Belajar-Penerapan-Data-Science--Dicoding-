# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

Jaya Jaya Maju merupakan salah satu perusahaan multinasional yang telah berdiri sejak tahun 2000. Ia memiliki lebih dari 1000 karyawan yang tersebar di seluruh penjuru negeri. 

Walaupun telah menjadi menjadi perusahaan yang cukup besar, Jaya Jaya Maju masih cukup kesulitan dalam mengelola karyawan. Hal ini berimbas tingginya attrition rate (rasio jumlah karyawan yang keluar dengan total karyawan keseluruhan) hingga lebih dari 10%.

Untuk mencegah hal ini semakin parah, manajer departemen HR ingin meminta bantuan Saya mengidentifikasi berbagai faktor yang mempengaruhi tingginya attrition rate tersebut. Selain itu, ia juga meminta Saya untuk membuat business dashboard untuk membantunya memonitori berbagai faktor tersebut.

### Permasalahan Bisnis

1. Faktor-faktor apa saja yang paling signifikan memicu karyawan untuk mengundurkan diri?

2. Kelompok demografi karyawan mana (usia, jabatan, status) yang paling rentan terhadap risiko attrition?

3. Bagaimana perusahaan dapat mendeteksi risiko pengunduran diri secara dini agar dapat melakukan tindakan preventif?

### Cakupan Proyek

1. **Analisis Data Eksploratif (EDA)**: Mengidentifikasi tren dan pola attrition berdasarkan data historis.

2. **Data Preprocessing**: Melakukan pembersihan data, encoding fitur kategori, dan penanganan ketidakseimbangan data (SMOTE).

3. **Machine Learning Modeling**: Membangun model prediksi menggunakan algoritma Random Forest untuk mendeteksi potensi attrition.

4. **Business Dashboard**: Membuat visualisasi interaktif untuk memonitor faktor pendorong attrition secara real-time.

### Persiapan

Sumber data: https://www.ibm.com/communities/analytics/watson-analytics-blog/watson-analytics-use-case-for-hr-retaining-valuable-employees/

Setup environment:

```
pip install pandas numpy scikit-learn matplotlib seaborn streamlit plotly joblib imbalanced-learn
```

## Business Dashboard

Business Dashboard dibuat menggunakan Streamlit dan Plotly. Dashboard ini dirancang agar departemen HR dapat melihat gambaran besar kesehatan SDM tanpa harus memahami kode teknis.

Fitur Dashboard:

- **Metrik Utama (KPI)**: Menampilkan total karyawan, persentase attrition rate, dan rata-rata pendapatan.

- **Analisis Rentang Usia**: Visualisasi yang menunjukkan distribusi pengunduran diri pada kelompok usia tertentu (misal: 18-25 tahun).

- **Dampak Lembur (OverTime)**: Grafik perbandingan yang membuktikan korelasi kuat antara beban kerja lembur dengan keputusan resign.

- **Analisis Jabatan (Job Role)**: Mengidentifikasi departemen atau posisi dengan tingkat attrition tertinggi untuk prioritas intervensi.

Link Dashboard: [https://a590-belajar-penerapan-data-science-fdzyhbzyacmc6anabpbnbs.streamlit.app/]

## Conclusion

Berdasarkan analisis data dan model Machine Learning yang dikembangkan, dapat disimpulkan bahwa:

1. **Faktor Utama**: Kebijakan lembur (OverTime) adalah pemicu tunggal terbesar yang menyebabkan karyawan memutuskan untuk keluar.

2. **Profil Berisiko**: Karyawan muda di rentang usia 18-25 tahun dengan status Single memiliki loyalitas yang paling rendah terhadap perusahaan.

3. **Departemen Kritis**: Posisi Sales Representative dan Laboratory Technician memiliki angka turnover tertinggi dibandingkan posisi manajerial.

### Rekomendasi Action Items (Optional)

Untuk menekan angka attrition, berikut adalah rekomendasi bagi perusahaan:

- **Evaluasi Work-Life Balance**: Mengurangi frekuensi lembur wajib dan memberikan kompensasi atau waktu istirahat tambahan bagi karyawan yang bekerja ekstra.
- **Program Retensi Karyawan Muda**: Membuat program mentorship dan jalur karir (career path) yang lebih jelas untuk meningkatkan keterikatan karyawan Gen Z dan Millennial awal.

- **Penyesuaian Insentif Departemen**: Melakukan peninjauan kembali terhadap skema bonus dan lingkungan kerja pada divisi Sales untuk meningkatkan kepuasan kerja di unit tersebut.
