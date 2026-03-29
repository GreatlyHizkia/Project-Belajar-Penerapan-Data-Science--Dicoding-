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

- Jalankan perintah berikut di terminal:
```
python -m venv venv
```

- Aktifkan environment:
    - Windows:
        ```
        venv\Scripts\activate
        ```

    - macOS/Linux:
        ```
        source venv/bin/activate
        ```

```
pip install pandas numpy scikit-learn matplotlib seaborn streamlit plotly joblib imbalanced-learn
```

- Instal Dependensi:
  
  Gunakan perintah berikut untuk menginstal seluruh library yang dibutuhkan secara otomatis melalui file `requirements.txt` 
  ```
  pip install -r requirements.txt
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

1. **Performa Model (Analisis Kuantitatif)**
Berdasarkan hasil pengujian menggunakan data uji (test set), model Random Forest yang telah dioptimalkan memberikan performa:
    - **Akurasi:** 80% (Model mampu memprediksi dengan tepat 80 dari 100 data)
    - **Precision (Class 1 - Resign): 41%,** model memiliki tantangan dalam menghindari false positive, namun tetap mampu memberikan peringatan dini.
    - **Recall (Class 1- Resign): 44%**, model mampu menangkap hampir setengah dari total karyawan yang sebenarnya akan melakukan attrition.
    - **F1-Score (Weighted Avg): 80%,** menunjukkan keseimbangan performa yang cukup stabil di antara kedua kelas (Stay & Resign).

2. **Insight Utama**
Berdasarkan hasil Feature Importance dari model Random Forest, ditemukan tiga faktor utama yang paling memengaruhi keputusan karyawan untuk mengundurkan diri:

    1. **Beban Kerja (OverTime):** Karyawan yang sering bekerja lembur memiliki korelasi yang sangat kuat dengan keputusan untuk resign.

    2. **Kelompok Usia:** Tingkat pengunduran diri tertinggi terkonsentrasi pada kelompok usia muda (18-25 tahun), yang menunjukkan adanya masalah pada retensi karyawan entry-level.

    3. **MonthlyIncome:** Pendapatan bulanan tetap menjadi faktor krusial. Karyawan dengan pendapatan yang tidak kompetitif lebih rentan untuk mencari peluang di luar perusahaan untuk memenuhi kebutuhan ekonomi mereka.


### Rekomendasi Action Items (Optional)

Berdasarkan hasil insight di atas, berikut adalah rekomendasi strategis bagi HR:

- **Review Kebijakan Lembur:**: Melakukan peninjauan ulang pembagian beban kerja untuk mengurangi ketergantungan pada lembur yang berlebihan guna menjaga *work-life balance*.

- **Program Career Path:**: Mengembangkan program pengembangan karir dan mentorship khusus untuk karyawan muda (Gen Z) guna meningkatkan keterikatan (engagement) mereka terhadap perusahaan.

- **Evaluasi Skala Upah:**: Melakukan salary benchmarking secara berkala, terutama bagi karyawan yang diprediksi berisiko tinggi oleh model, untuk memastikan kompensasi tetap kompetitif di pasar.



### Cara menjalankan script Python (predict.py)
1. **Persiapkan Data:**
    
    Pastikan model (`model_attrition.pkl`) dan daftar fitur (`features_list.pkl`) berada dalam folder yang sama dengan script `predict.py`
2. **Jalankan Command:**
    Buka terminal atau command prompt, lalu ketikkan perintah berikut:
    ```
    python predict.py
    ```
3. **Input Data:**
    Script akan meminta untuk memasukkan nilai untuk beberapa fitur utama (seperti *Overtime*, *MonthlyIncome*, *TotalWorkingYears*, dll). Ikuti instruksi yang muncul di terminal untuk mendapatkan hasil prediksi apakah karyawan tersebut berpotensi *Resign* atau *Stay*.