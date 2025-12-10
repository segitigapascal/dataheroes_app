import streamlit as st
from utils.helpers import simpan_jawaban

st.title("📗 LKM Pertemuan 2 – Pengolahan Data (Tabel & Diagram)")

kelompok = st.selectbox("Pilih Kelompok", list(st.session_state.data_kelompok.keys()))
data_kel = st.session_state.data_kelompok[kelompok]
st.info(f"Kelompok {kelompok} – {data_kel['nama']}")

st.text_area("Masukkan data hasil angket/wawancara:", key=f"data2_{kelompok}")

st.markdown("""
Langkah kegiatan:
1. Masukkan data ke Google Sheet  
2. Susun tabel distribusi frekuensi untuk setiap pertanyaan skala dan tertutup  
3. Buat minimal 2 diagram berbeda (batang, lingkaran, garis, histogram)  
4. Bandingkan setiap diagram: apa bedanya? Mana lebih mudah dipahami?  
5. Diskusikan diagram paling tepat, jelaskan alasannya  
6. Bagikan Google Sheet ke guru melalui email
""")
st.text_input("Link Google Sheet kelompok:", key=f"link_sheet_{kelompok}")

if st.button("Simpan Pertemuan 2"):
    data = {k:v for k,v in st.session_state.items() if f"_{kelompok}" in k}
    simpan_jawaban("pertemuan_2", kelompok, data)
    st.success("Jawaban Pertemuan 2 tersimpan!")
