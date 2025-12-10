import streamlit as st

def simpan_jawaban(pertemuan, kelompok, data):
    """
    Simpan jawaban murid ke session_state.
    """
    if "jawaban" not in st.session_state:
        st.session_state.jawaban = {}
    key = f"{pertemuan}_{kelompok}"
    st.session_state.jawaban[key] = data

def ambil_jawaban(pertemuan, kelompok):
    """
    Ambil jawaban murid dari session_state.
    """
    key = f"{pertemuan}_{kelompok}"
    return st.session_state.get("jawaban", {}).get(key, {})
