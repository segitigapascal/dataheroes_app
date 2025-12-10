# app.py
import streamlit as st

st.set_page_config(page_title="Data Heroes", layout="wide")

purple_css = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600&display=swap');
html, body, [class*="css"]  {
    font-family: 'Poppins', sans-serif !important;
}
.main {
    background: linear-gradient(135deg, #F7F3FF 0%, #E9DFFF 40%, #F1EAFF 100%);
}
.block-container { padding-top: 1rem; }
h1,h2,h3 { color: #5E3C99; font-weight:600; }
.stat-card {
    padding: 18px;
    border-radius: 12px;
    background: rgba(255,255,255,0.6);
    backdrop-filter: blur(6px);
    border: 1px solid #e9dbff;
    box-shadow: 0 6px 18px rgba(110,70,150,0.06);
    margin-bottom: 16px;
}
.stButton>button { background: #7e57c2; color: white; border-radius: 10px; }
hr { height:1px; border:0; background: linear-gradient(to right,#c9b5f4,#7e57c2,#c9b5f4); margin:16px 0; }
</style>
"""
st.markdown(purple_css, unsafe_allow_html=True)

st.title("🦸 DATA HEROES — LKM Statistik Digital")
st.subheader("Menyulap Data Mentah Jadi Presentasi Keren!")

st.markdown(
    """
    **Panduan singkat:**  
    - Buka halaman *Daftar Kelompok* untuk membuat slot kelompok.  
    - Kelompok buka *LKM Kelompok* untuk mengisi identitas dan LKM 3 pertemuan.  
    - Gunakan *Kamus* untuk mengklasifikasi jawaban.  
    - Gunakan *Rekomendasi Grafik* untuk ide visualisasi di pertemuan 3.  
    - Setiap kelompok bisa export PDF di halaman LKM.
    """
)
st.info("Tema: soft purple. UI telah disesuaikan untuk tampilan kelas.")
