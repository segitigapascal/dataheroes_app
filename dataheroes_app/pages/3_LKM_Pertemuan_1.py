import streamlit as st
from utils.helpers import simpan_jawaban

st.title("📘 LKM Pertemuan 1 – Identifikasi & Klasifikasi Data")

kelompok = st.selectbox("Pilih Kelompok", list(st.session_state.data_kelompok.keys()))
data_kel = st.session_state.data_kelompok[kelompok]
st.info(f"Kelompok {kelompok} – {data_kel['nama']}")

# Masalah
st.subheader("Masalah dan Pertanyaan Mendasar")
st.text_area("Tantangan: Bagaimana cara mengukur persepsi warga sekolah dan masyarakat?", key=f"tantangan1_{kelompok}")

# Kamus
st.subheader("📚 Kamus Jenis Data & Skala Pengukuran")
kamus = {
    "Data Kuantitatif": "Data berupa angka. Contoh: kepuasan rasa (1–5)",
    "Data Kualitatif": "Data berupa kategori/sifat. Contoh: kesan positif/negatif",
    "Skala Nominal": "Kategori tanpa urutan. Contoh: jenis kelamin, status",
    "Skala Ordinal": "Kategori berurutan. Contoh: sangat puas → sangat tidak puas",
    "Skala Interval": "Angka berjarak sama tapi tanpa nol mutlak. Contoh: suhu celcius",
    "Skala Rasio": "Angka berjarak sama dengan nol mutlak. Contoh: tinggi badan, berat badan"
}
for istilah, arti in kamus.items():
    st.markdown(f"**{istilah}:** {arti}")

# Kegiatan 1
st.subheader("Kegiatan 1 – Diskusi Informasi Penting")
st.text_area("Data penting yang dikumpulkan:", key=f"kegiatan1_{kelompok}")

# Kegiatan 2
st.subheader("Kegiatan 2 – Tabel Klasifikasi Data")
for i in range(1,9):
    st.text_input(f"No {i} – Data yang Dikumpulkan", key=f"data{i}_{kelompok}")
    st.selectbox("Jenis Data", ["Kualitatif", "Kuantitatif"], key=f"jenis_data{i}_{kelompok}")
    st.text_input("Catatan (gunakan Kamus sebagai referensi)", key=f"catatan{i}_{kelompok}")

# Kegiatan 3
st.subheader("Kegiatan 3 – Pertanyaan Survei")
st.markdown("Buat 10 pertanyaan: 2 tertutup, 6 skala (1–5), 2 terbuka")
for i in range(1,11):
    st.selectbox(f"No {i} – Jenis Pertanyaan", ["Tertutup", "Skala", "Terbuka"], key=f"jenis_pertanyaan{i}_{kelompok}")
    st.text_input(f"Pertanyaan", key=f"pertanyaan{i}_{kelompok}")
    st.selectbox(f"Jenis Data", ["Kualitatif", "Kuantitatif"], key=f"jenis_data_pertanyaan{i}_{kelompok}")
    st.text_input(f"Jenis Skala Pengukuran", key=f"skala{i}_{kelompok}")

# Kegiatan 4
st.subheader("Kegiatan 4 – Google Form")
st.text_input("Link Google Form yang dibuat:", key=f"link_form_{kelompok}")

# Kesimpulan
st.subheader("Kesimpulan")
st.text_area("a. Data kualitatif adalah", key=f"kesimpulan_qual_{kelompok}")
st.text_area("b. Data kuantitatif adalah", key=f"kesimpulan_quant_{kelompok}")
st.text_area("c. Skala nominal adalah", key=f"kesimpulan_nominal_{kelompok}")
st.text_area("d. Skala ordinal adalah", key=f"kesimpulan_ordinal_{kelompok}")
st.text_area("e. Skala interval adalah", key=f"kesimpulan_interval_{kelompok}")
st.text_area("f. Skala rasio adalah", key=f"kesimpulan_rasio_{kelompok}")

if st.button("Simpan Pertemuan 1"):
    data = {k:v for k,v in st.session_state.items() if f"_{kelompok}" in k}
    simpan_jawaban("pertemuan_1", kelompok, data)
    st.success("Jawaban Pertemuan 1 tersimpan!")
