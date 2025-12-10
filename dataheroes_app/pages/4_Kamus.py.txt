# pages/4_Kamus.py
import streamlit as st
from utils import klasifikasi_jawaban

st.title("📚 Kamus — Klasifikasi Jenis Data & Skala")

jaw = st.text_area("Masukkan contoh jawaban (mis. '4', 'sangat puas', 'plastik', 'ya')")

if st.button("Klasifikasi"):
    res = klasifikasi_jawaban(jaw)
    st.markdown(f"""
    <div class="stat-card">
    <h3>Hasil Klasifikasi</h3>
    <b>Jenis Data:</b> {res['jenis_data']}<br>
    <b>Skala:</b> {res['skala']}<br>
    <b>Jenis Skala:</b> {res['tipe_skala']}<br>
    <b>Alasan:</b> {res['alasan']}
    </div>
    """, unsafe_allow_html=True)
