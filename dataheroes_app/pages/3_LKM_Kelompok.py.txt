# pages/3_LKM_Kelompok.py
import streamlit as st
from utils import klasifikasi_jawaban, rekomendasi_grafik, generate_pdf_for_group

st.title("📘 LKM Kelompok")

if "jumlah_kelompok" not in st.session_state or st.session_state["jumlah_kelompok"] == 0:
    st.warning("Silakan atur jumlah kelompok terlebih dahulu pada halaman 'Daftar Kelompok'.")
    st.stop()

# pilih kelompok
kel = st.selectbox("Pilih kelompok", list(range(1, st.session_state["jumlah_kelompok"]+1)))
key = f"kel_{kel}"
group = st.session_state.get(key, {"meta": {"Kelompok": kel}})

# wrapper card
st.markdown('<div class="stat-card">', unsafe_allow_html=True)
st.subheader(f"Identitas Kelompok {kel}")
nama = st.text_input("Nama Kelompok", value=group["meta"].get("Nama Kelompok",""))
kelas = st.text_input("Kelas", value=group["meta"].get("Kelas",""))
anggota = st.text_area("Nama Anggota (pisahkan baris)", value=group["meta"].get("Anggota",""))
if st.button("Simpan Identitas"):
    st.session_state[key]["meta"].update({"Nama Kelompok": nama, "Kelas": kelas, "Anggota": anggota})
    st.success("Identitas tersimpan.")
st.markdown('</div>', unsafe_allow_html=True)

# tabs pertemuan
tab1, tab2, tab3 = st.tabs(["Pertemuan 1", "Pertemuan 2", "Pertemuan 3"])

with tab1:
    st.markdown("### Pertemuan 1 — Identifikasi & Klasifikasi Data")
    st.write("Isi delapan data pilihan (satu baris per data):")
    data8 = st.text_area("8 Data", value="\n".join(group["lkm"].get("pert1_data8", [])))
    st.write("Masukkan 10 pertanyaan angket (satu baris per pertanyaan):")
    q10 = st.text_area("10 Pertanyaan", value="\n".join(group["lkm"].get("pert1_q10", [])))
    gf = st.text_input("Link Google Form (opsional)", value=group["lkm"].get("pert1_gform",""))
    if st.button("Simpan Pertemuan 1"):
        st.session_state[key]["lkm"]["pert1_data8"] = [x.strip() for x in data8.splitlines() if x.strip()]
        st.session_state[key]["lkm"]["pert1_q10"] = [x.strip() for x in q10.splitlines() if x.strip()]
        st.session_state[key]["lkm"]["pert1_gform"] = gf
        st.success("Pertemuan 1 tersimpan.")

    st.markdown("---")
    st.markdown("#### Gunakan Kamus untuk mengklasifikasikan contoh jawaban")
    instr = st.text_input("Instrumen contoh:")
    contoh = st.text_input("Contoh jawaban:")
    if st.button("Analisis Jenis Data"):
        res = klasifikasi_jawaban(contoh)
        st.markdown(f"""<div class="stat-card"><b>Jenis Data:</b> {res['jenis_data']}<br><b>Skala:</b> {res['skala']}<br><b>Jenis Skala:</b> {res['tipe_skala']}<br><b>Alasan:</b> {res['alasan']}</div>""", unsafe_allow_html=True)

with tab2:
    st.markdown("### Pertemuan 2 — Pengolahan Data")
    st.write("Anda dapat menempel link Google Sheet hasil input data di sini atau ringkasan tabel.")
    gs = st.text_input("Link Google Sheet", value=group["lkm"].get("pert2_gsheet",""))
    cat2 = st.text_area("Catatan hasil pengolahan", value=group["lkm"].get("pert2_catatan",""))
    if st.button("Simpan Pertemuan 2"):
        st.session_state[key]["lkm"]["pert2_gsheet"] = gs
        st.session_state[key]["lkm"]["pert2_catatan"] = cat2
        st.success("Pertemuan 2 tersimpan.")

with tab3:
    st.markdown("### Pertemuan 3 — Visualisasi & Analisis")
    ringkasan = st.text_area("Ringkasan analisis", value=group["lkm"].get("pert3_ringkasan",""))
    grafik_pilihan = st.text_input("Grafik pilihan & alasan", value=group["lkm"].get("pert3_grafik",""))
    if st.button("Simpan Pertemuan 3"):
        st.session_state[key]["lkm"]["pert3_ringkasan"] = ringkasan
        st.session_state[key]["lkm"]["pert3_grafik"] = grafik_pilihan
        st.success("Pertemuan 3 tersimpan.")

    st.markdown("---")
    st.markdown("#### Rekomendasi Grafik Otomatis")
    p3_q = st.text_input("Pertanyaan (contoh)")
    p3_a = st.text_area("Contoh jawaban (pisahkan koma/newline)")
    audiens = st.selectbox("Audiens pengisi", ["Santri","Staf","Pengunjung","Orang Tua","Alumni"])
    if st.button("Dapatkan Rekomendasi Grafik"):
        hasil = rekomendasi_grafik(p3_q, p3_a, audiens)
        for h in hasil:
            st.markdown(f"""<div class="stat-card"><h4>{h['grafik']}</h4><b>Alasan:</b> {h['kenapa']}<br><b>Kapan:</b> {h['kapan']}<br><i>{h['saran_presentasi']}</i></div>""", unsafe_allow_html=True)

# Export PDF di sidebar
st.sidebar.markdown('<div class="stat-card"><h4>📄 Export / Cetak</h4><p>Export PDF ringkasan LKM kelompok ini.</p></div>', unsafe_allow_html=True)
if st.sidebar.button("Export PDF Kelompok Ini"):
    group_meta = st.session_state[key]["meta"]
    lkm_answers = st.session_state[key]["lkm"]
    pdf_bytes = generate_pdf_for_group(group_meta, {
        "Pertemuan 1": {
            "Data yang dipilih": "\n".join(lkm_answers.get("pert1_data8", [])),
            "Pertanyaan": "\n".join(lkm_answers.get("pert1_q10", [])),
            "Google Form": lkm_answers.get("pert1_gform","")
        },
        "Pertemuan 2": {
            "Google Sheet": lkm_answers.get("pert2_gsheet",""),
            "Catatan": lkm_answers.get("pert2_catatan","")
        },
        "Pertemuan 3": {
            "Ringkasan": lkm_answers.get("pert3_ringkasan",""),
            "Grafik Pilihan": lkm_answers.get("pert3_grafik","")
        }
    })
    st.sidebar.success("PDF siap diunduh.")
    st.sidebar.download_button("⬇️ Download PDF Kelompok", data=pdf_bytes, file_name=f"DataHeroes_Kelompok{kel}.pdf", mime="application/pdf")
