import streamlit as st
from utils.helpers import simpan_jawaban

st.title("👥 Daftar Kelompok (Guru)")

jumlah = st.number_input("Masukkan jumlah kelompok:", min_value=1, step=1)

if "data_kelompok" not in st.session_state:
    st.session_state.data_kelompok = {}

for i in range(1, jumlah + 1):
    st.subheader(f"Kelompok {i}")
    nama = st.text_input(f"Nama Kelompok {i}", key=f"nama_{i}")
    kelas = st.text_input(f"Kelas Kelompok {i}", key=f"kelas_{i}")
    anggota = st.text_area(f"Anggota Kelompok {i} (pisahkan dengan enter)", key=f"anggota_{i}")

    st.session_state.data_kelompok[i] = {
        "nama": nama,
        "kelas": kelas,
        "anggota": anggota.split("\n")
    }

if st.button("Simpan Daftar Kelompok"):
    simpan_jawaban("daftar_kelompok", "all", st.session_state.data_kelompok)
    st.success("Daftar kelompok tersimpan!")
