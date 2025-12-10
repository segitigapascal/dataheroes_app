import streamlit as st

st.set_page_config(page_title="LKM Per Kelompok", page_icon="📘")

st.title("📘 LKM Per Kelompok")

# Cek apakah data kelompok tersedia
if "data_kelompok" not in st.session_state:
    st.warning("❗ Data kelompok belum diisi. Silakan buka halaman 'Daftar Kelompok'.")
    st.stop()

# Pilih kelompok
pilihan = st.selectbox(
    "Pilih Kelompok:",
    [f"Kelompok {d['Kelompok']} - {d['Nama']}" for d in st.session_state["data_kelompok"]]
)

idx = int(pilihan.split()[1]) - 1
data = st.session_state["data_kelompok"][idx]

st.subheader(f"📘 LKM — {data['Nama']}")

st.write("### Identitas Kelompok")
st.write(f"**Nama Kelompok:** {data['Nama']}")
st.write(f"**Kelas:** {data['Kelas']}")
st.write(f"**Anggota:** {data['Anggota']}")

st.write("---")
st.write("## 📝 Jawaban LKM")

jawaban1 = st.text_area("1. Apa itu data kuantitatif?", key=f"lkm1_{idx}")
jawaban2 = st.text_area("2. Apa itu data kualitatif?", key=f"lkm2_{idx}")

if st.button("💾 Simpan Jawaban LKM", key=f"simpan_lkm_{idx}"):
    if "jawaban_lkm" not in st.session_state:
        st.session_state["jawaban_lkm"] = {}

    st.session_state["jawaban_lkm"][idx] = {
        "jawaban1": jawaban1,
        "jawaban2": jawaban2
    }

    st.success("Jawaban berhasil disimpan!")

if "jawaban_lkm" in st.session_state and idx in st.session_state["jawaban_lkm"]:
    st.write("### 📄 Jawaban Tersimpan:")
    st.json(st.session_state["jawaban_lkm"][idx])
