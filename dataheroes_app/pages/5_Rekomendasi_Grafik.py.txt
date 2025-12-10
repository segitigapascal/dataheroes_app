# pages/5_Rekomendasi_Grafik.py
import streamlit as st
from utils import rekomendasi_grafik

st.title("📊 Rekomendasi Grafik Otomatis")

pert = st.text_input("Pertanyaan (opsional)")
jaw = st.text_area("Contoh jawaban (pisahkan koma/newline)")
aud = st.selectbox("Audiens:", ["Santri","Staf","Pengunjung","Orang Tua","Alumni"])

if st.button("Dapatkan Rekomendasi"):
    hasil = rekomendasi_grafik(pert, jaw, aud)
    for h in hasil:
        st.markdown(f"""
        <div class="stat-card">
        <h4>📈 {h['grafik']}</h4>
        <b>Alasan:</b> {h['kenapa']}<br>
        <b>Kapan:</b> {h['kapan']}<br>
        <i>{h['saran_presentasi']}</i>
        </div>
        """, unsafe_allow_html=True)
