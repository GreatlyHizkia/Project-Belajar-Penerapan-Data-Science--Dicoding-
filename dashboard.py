import streamlit as st
import pandas as pd
import plotly.express as px

# 1. KONFIGURASI HALAMAN
st.set_page_config(
    page_title="HR Attrition Business Dashboard",
    page_icon="📊",
    layout="wide"
)

# 2. LOAD & PREPROCESS DATA
@st.cache_data
def load_data():
    # Ganti dengan nama file dataset Anda
    df = pd.read_csv('employee_df_clean.csv')
    
    # A. Memastikan Attrition berupa label teks (Yes/No)
    if df['Attrition'].dtype != 'object':
        df['Attrition'] = df['Attrition'].map({1: 'Yes', 0: 'No'})
    
    # B. MEMBUAT RENTANG USIA (Binning)
    # Membuat kategori agar grafik lebih bersih dan informatif
    bins = [18, 26, 36, 46, 61]
    labels = ['18-25 (Young)', '26-35 (Early Career)', '36-45 (Mid Career)', '46+ (Senior)']
    df['Age_Range'] = pd.cut(df['Age'], bins=bins, labels=labels, right=False)
    
    return df

try:
    df = load_data()
except Exception as e:
    st.error(f"Gagal memuat file. Pastikan 'employee_data.csv' ada di folder yang sama. Error: {e}")
    st.stop()

# 3. HEADER
st.title("🏢 HR Business Intelligence Dashboard")
st.markdown("Analisis Faktor Pendorong *Employee Attrition* untuk Strategi Retensi Karyawan.")

# 4. BARIS 1: KPI (Key Performance Indicators)
st.divider()
col1, col2, col3, col4 = st.columns(4)

total_emp = len(df)
attr_yes = len(df[df['Attrition'] == 'Yes'])
attr_rate = (attr_yes / total_emp) * 100
avg_income = df['MonthlyIncome'].mean()

with col1:
    st.metric("Total Employees", f"{total_emp}")
with col2:
    st.metric("Attrition Count", f"{attr_yes}", delta_color="inverse")
with col3:
    st.metric("Attrition Rate", f"{attr_rate:.1f}%")
with col4:
    st.metric("Avg. Monthly Income", f"${avg_income:,.0f}")

st.divider()

# 5. BARIS 2: ANALISIS RENTANG USIA & LEMBUR
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("📌 Attrition berdasarkan Rentang Usia")
    # Histogram dengan urutan kategori yang benar
    fig_age = px.histogram(
        df, 
        x="Age_Range", 
        color="Attrition",
        barmode="group",
        text_auto=True,
        color_discrete_map={'Yes': '#EF553B', 'No': '#636EFA'},
        category_orders={"Age_Range": ['18-25 (Young)', '26-35 (Early Career)', '36-45 (Mid Career)', '46+ (Senior)']}
    )
    fig_age.update_layout(xaxis_title="Rentang Usia", yaxis_title="Jumlah Karyawan")
    st.plotly_chart(fig_age, use_container_width=True)

with col_right:
    st.subheader("📌 Persentase Resign per Kebijakan Lembur")
    # Menghitung proporsi resign di dalam kelompok OverTime
    ot_analysis = df.groupby('OverTime')['Attrition'].value_counts(normalize=True).unstack() * 100
    
    fig_ot = px.bar(
        ot_analysis, 
        y='Yes', 
        text_auto='.1f',
        labels={'Yes': 'Persentase Resign (%)'},
        color_discrete_sequence=['#EF553B']
    )
    fig_ot.update_layout(showlegend=False, xaxis_title="Melakukan Lembur (OverTime)")
    st.plotly_chart(fig_ot, use_container_width=True)

# 6. BARIS 3: ANALISIS PER JABATAN (JOB ROLE)
st.divider()
st.subheader("📌 Total Karyawan Resign per Jabatan (Job Role)")

# Filter hanya yang resign untuk melihat beban departemen
job_attr = df[df['Attrition'] == 'Yes']['JobRole'].value_counts().reset_index()
job_attr.columns = ['JobRole', 'Total_Resign']

fig_role = px.bar(
    job_attr, 
    x='Total_Resign', 
    y='JobRole', 
    orientation='h',
    text_auto=True,
    color='Total_Resign',
    color_continuous_scale='Reds'
)
st.plotly_chart(fig_role, use_container_width=True)

# 7. KESIMPULAN STRATEGIS
st.divider()
with st.expander("💡 Analisis & Rekomendasi Bisnis (Untuk Laporan)"):
    st.write(f"""
    1. **Tingkat Attrition:** Saat ini berada pada **{attr_rate:.1f}%**. Fokus perbaikan pada kelompok berisiko tinggi.
    2. **Kelompok Usia Berisiko:** Karyawan di rentang **18-25 tahun** memiliki kecenderungan keluar yang signifikan. Rekomendasi: Program pengembangan karir awal (*fast-track*).
    3. **Isu Work-Life Balance:** Karyawan yang mendapatkan beban **OverTime** terbukti secara data lebih banyak yang mengundurkan diri.
    4. **Departemen Prioritas:** Posisi dengan angka resign tertinggi (lihat grafik bar merah) memerlukan evaluasi beban kerja atau penyesuaian insentif.
    """)

st.caption("Submission Proyek Akhir - Pengembangan Dashboard HR")