import streamlit as st
from utils.helpers import simpan_jawaban

st.title("📙 LKM Pertemuan 3 – Analisis & Interpretasi Data")

kelompok = st.selectbox("Pilih Kelompok", list(st.session_state.data_kelompok.keys()))
data_kel = st.session_state.data_kelompok[kelompok]
st.info(f"Kelompok {kelompok} – {data_kel['nama']}")

st.text_area("Masukkan data tabel & diagram:", key=f"data3_{kelompok}")

st.subheader("Analisis")
st.text_area("1. Pola apa yang terlihat? Adakah data yang dominan?", key=f"pola_{kelompok}")
st.text_area("2. Analisis persepsi positif, netral, negatif", key=f"analisis_{kelompok}")
st.text_area("3. Pilih diagram terbaik dan jelaskan alasannya", key=f"diagram_{kelompok}")

# Rekomendasi Grafik
st.subheader("📊 Rekomendasi Grafik (Untuk LKPM)")
rekomendasi_grafik = {
    "Data Kuantitatif Diskrit": "Diagram Batang / Histogram",
    "Data Kuantitatif Kontinu": "Histogram / Poligon Frekuensi",
    "Data Kualitatif Nominal": "Diagram Batang / Diagram Lingkaran",
    "Data Kualitatif Ordinal": "Diagram Batang Berurutan / Lingkaran"
}
for tipe, grafik in rekomendasi_grafik.items():
    st.markdown(f"**{tipe}:** {grafik}")

st.text_area("Tuliskan grafik yang seharusnya dibuat berdasarkan data kalian (LKPM):", key=f"grafik_LKPM_{kelompok}")

st.subheader("Kesimpulan & Rekomendasi")
st.text_area("4. Kesimpulan dan rekomendasi perbaikan kafe ABS", key=f"kesimpulan3_{kelompok}")

st.subheader("Hasil Presentasi")
st.markdown("""
5. Susun laporan mini riset dalam bentuk presentasi (tabel & diagram)  
6. Presentasikan hasil riset di depan kelas
""")

if st.button("Simpan Pertemuan 3"):
    data = {k:v for k,v in st.session_state.items() if f"_{kelompok}" in k}
    simpan_jawaban("pertemuan_3", kelompok, data)
    st.success("Jawaban Pertemuan 3 tersimpan!")
