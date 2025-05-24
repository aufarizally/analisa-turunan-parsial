import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Fungsi perhitungan
def total_waktu_produksi(x, y):
    return 2 * x*2 + 3 * x * y + y*2

def turunan_parsial(x, y):
    dT_dx = 4 * x + 3 * y
    dT_dy = 3 * x + 2 * y
    return dT_dx, dT_dy

def waktu_baku(waktu_normal, toleransi):
    return waktu_normal * (1 + toleransi)

# Judul Aplikasi
st.title("🚗 Aplikasi Analisis Waktu Baku Produksi Mobil")

# Sidebar Input
st.sidebar.header("📥 Input Aktivitas Produksi")
x = st.sidebar.number_input("Waktu Perakitan Mesin (x) [jam]", min_value=0.0, value=2.0, step=0.5)
y = st.sidebar.number_input("Waktu Pemasangan Bodi (y) [jam]", min_value=0.0, value=3.0, step=0.5)
toleransi_persen = st.sidebar.slider("Toleransi (%)", min_value=0, max_value=30, value=15)

# Opsional tambahan
jumlah_pekerja = st.sidebar.slider("Jumlah Pekerja", 1, 100, 10)
jam_kerja_per_hari = st.sidebar.slider("Jam Kerja per Hari", 4, 24, 8)

# Perhitungan dasar
waktu_total = total_waktu_produksi(x, y)
dT_dx, dT_dy = turunan_parsial(x, y)
wb = waktu_baku(waktu_total, toleransi_persen / 100)

# Total jam kerja harian
total_jam_harian = jumlah_pekerja * jam_kerja_per_hari

# Output produksi
unit_mobil_harian = total_jam_harian / wb if wb > 0 else 0
unit_mesin_harian = (jumlah_pekerja * jam_kerja_per_hari) / x if x > 0 else 0

# Tampilkan hasil perhitungan
st.header("📊 Hasil Perhitungan Produksi")
st.write(f"*Total Waktu Produksi (T):* {waktu_total:.2f} jam")
st.write(f"*Turunan Parsial terhadap x (∂T/∂x):* {dT_dx:.2f}")
st.write(f"*Turunan Parsial terhadap y (∂T/∂y):* {dT_dy:.2f}")
st.write(f"*Toleransi:* {toleransi_persen}%")
st.write(f"*Waktu Baku (WB):* {wb:.2f} jam")

# Rumus latex
st.subheader("🧮 Rumus Waktu Baku")
st.latex(r'''
\text{Waktu Baku (WB)} = \text{Waktu Normal (WN)} \times (1 + \text{Toleransi})
''')
st.latex(fr'''
WB = {waktu_total:.2f} \times (1 + {toleransi_persen / 100:.2f}) = {wb:.2f} \ \text{{jam}}
''')

# Grafik batang turunan parsial
st.subheader("📈 Grafik Pengaruh Aktivitas terhadap Waktu Produksi")
fig, ax = plt.subplots()
aktivitas = ['Perakitan Mesin (x)', 'Pemasangan Bodi (y)']
pengaruh = [dT_dx, dT_dy]
warna = ['#FF6F61', '#6BAED6']

bars = ax.bar(aktivitas, pengaruh, color=warna)
ax.set_ylabel("Pengaruh terhadap Total Waktu (jam)")
ax.set_title("Turunan Parsial ∂T/∂x dan ∂T/∂y")
ax.grid(True, axis='y', linestyle='--', alpha=0.6)

for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval + 0.5, f'{yval:.1f}', ha='center', va='bottom', fontweight='bold')

st.pyplot(fig)

# Output Produksi
st.subheader("🚀 Estimasi Produksi Harian")
st.write(f"*Jumlah Pekerja:* {jumlah_pekerja} orang")
st.write(f"*Jam Kerja per Hari:* {jam_kerja_per_hari} jam")
st.write(f"*Total Jam Kerja Harian:* {total_jam_harian} jam")
st.write(f"*Mobil yang Bisa Dirakit per Hari:* {unit_mobil_harian:.2f} unit")
st.write(f"*Unit Mesin yang Dirakit (x = {x} jam):* {unit_mesin_harian:.0f} unit per hari")

# Contoh Kasus Naratif
st.markdown("---")
st.subheader("📌 Contoh Interpretasi")
st.markdown(f"""
Jika terdapat *{jumlah_pekerja} orang pekerja, masing-masing bekerja selama **{jam_kerja_per_hari} jam per hari*, 
dan waktu baku perakitan mobil adalah *{wb:.2f} jam*, maka dalam sehari dapat diselesaikan sekitar 
*{unit_mobil_harian:.2f} unit mobil lengkap*.

Sementara itu, untuk proses perakitan mesin yang membutuhkan *{x} jam per unit*, maka tim produksi mampu menyelesaikan 
sekitar *{unit_mesin_harian:.0f} unit mesin per hari*.
""")

# =======================
# Tambahan: Tabel Simulasi Variasi Input
# =======================
st.markdown("---")
st.subheader("📋 Tabel Simulasi Variasi Input")

# Range variasi simulasi
toleransi_range = np.arange(0, 31, 5)       # 0,5,10,...,30%
pekerja_range = np.arange(5, 51, 5)         # 5,10,...,50 orang
jam_kerja_range = np.arange(4, 13, 2)       # 4,6,8,10,12 jam kerja

data_simulasi = []

for tol in toleransi_range:
    for pekerja in pekerja_range:
        for jam_kerja in jam_kerja_range:
            wb_sim = waktu_baku(waktu_total, tol/100)
            total_jam = pekerja * jam_kerja
            unit_harian = total_jam / wb_sim if wb_sim > 0 else 0
            
            data_simulasi.append({
                "Toleransi (%)": tol,
                "Jumlah Pekerja": pekerja,
                "Jam Kerja per Hari": jam_kerja,
                "Waktu Baku (jam)": round(wb_sim, 2),
                "Total Jam Kerja (jam)": total_jam,
                "Unit Mobil per Hari": round(unit_harian, 2)
            })

df_simulasi = pd.DataFrame(data_simulasi)

st.dataframe(df_simulasi.style.format({
    "Waktu Baku (jam)": "{:.2f}",
    "Unit Mobil per Hari": "{:.2f}",
    "Total Jam Kerja (jam)": "{:.0f}"
}))
