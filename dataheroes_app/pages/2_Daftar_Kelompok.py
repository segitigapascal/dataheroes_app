import streamlit as st

st.set_page_config(page_title="Daftar Kelompok", page_icon="👥")

st.title("👥 Daftar Kelompok (Guru)")

jumlah = st.number_input("Masukkan jumlah kelompok:", min_value=1, step=1)

st.write("---")

# Form input data kelompok
for i in range(1, jumlah + 1):
    st.subheader(f"Kelompok {i}")
    st.text_input(f"Nama Kelompok {i}", key=f"nama_{i}")
    st.text_input(f"Kelas Kelompok {i}", key=f"kelas_{i}")
    st.text_area(f"Anggota Kelompok {i}", key=f"anggota_{i}")

st.write("---")

# Tombol simpan
if st.button("💾 Simpan Semua Data"):
    st.session_state["data_kelompok"] = []

    for i in range(1, jumlah + 1):
        st.session_state["data_kelompok"].append({
            "Kelompok": i,
            "Nama": st.session_state.get(f"nama_{i}", ""),
            "Kelas": st.session_state.get(f"kelas_{i}", ""),
            "Anggota": st.session_state.get(f"anggota_{i}", "")
        })

    st.success("Data kelompok berhasil disimpan!")
    st.json(st.session_state["data_kelompok"])
