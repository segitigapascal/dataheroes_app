# pages/2_Daftar_Kelompok.py
import streamlit as st

st.title("👥 Daftar Kelompok (Guru)")

if "jumlah_kelompok" not in st.session_state:
    st.session_state["jumlah_kelompok"] = 0

col1, col2 = st.columns([3,1])
with col1:
    jumlah = st.number_input("Masukkan jumlah kelompok:", min_value=1, value=int(st.session_state.get("jumlah_kelompok",1)), step=1)
with col2:
    if st.button("Buat / Update"):
        st.session_state["jumlah_kelompok"] = int(jumlah)
        # inisialisasi storage per kelompok
        for i in range(1, int(jumlah)+1):
            key = f"kel_{i}"
            if key not in st.session_state:
                st.session_state[key] = {
                    "meta": {"Kelompok": i, "Nama Kelompok": f"Kelompok {i}", "Kelas": "", "Anggota": ""},
                    "lkm": {}
                }
        st.success(f"Jumlah kelompok diatur ke {jumlah}")
st.markdown("#### Status penyimpanan sementara (session):")
st.json({k: v for k, v in st.session_state.items() if k.startswith("kel_")})
