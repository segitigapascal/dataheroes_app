# utils.py
import re
import io
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
import datetime

# -----------------------
# pola & kata kunci
# -----------------------
likert_patterns = [
    "sangat tidak setuju", "tidak setuju", "netral", "setuju", "sangat setuju",
    "sangat puas", "puas", "tidak puas", "sangat baik", "baik", "kurang"
]
ya_tidak = ["ya", "tidak", "iya", "bukan"]
nominal_keywords = ["plastik", "kertas", "organik", "anorganik", "warna", "merek", "jenis", "laki", "perempuan"]

# -----------------------
# klasifikasi jawaban
# -----------------------
def klasifikasi_jawaban(jawaban: str) -> dict:
    j = str(jawaban or "").lower().strip()

    for pola in likert_patterns:
        if pola in j:
            return {
                "jenis_data": "Kualitatif",
                "skala": "Ordinal",
                "tipe_skala": "Skala Likert (Ordinal)",
                "alasan": "Mengandung kata kunci tingkatan (Likert)."
            }

    if j in ya_tidak:
        return {
            "jenis_data": "Kualitatif",
            "skala": "Nominal",
            "tipe_skala": "Dikotomi (Ya/Tidak)",
            "alasan": "Jawaban berupa dua kategori tanpa urutan."
        }

    if re.fullmatch(r"^-?\d+(\.\d+)?$", j):
        return {
            "jenis_data": "Kuantitatif",
            "skala": "Rasio",
            "tipe_skala": "Numerik (Rasio)",
            "alasan": "Jawaban berupa angka murni."
        }

    if re.search(r"\d+", j):
        return {
            "jenis_data": "Kuantitatif",
            "skala": "Rasio",
            "tipe_skala": "Numerik (mengandung angka)",
            "alasan": "Jawaban mengandung angka sehingga dianggap numerik."
        }

    for kata in nominal_keywords:
        if kata in j:
            return {
                "jenis_data": "Kualitatif",
                "skala": "Nominal",
                "tipe_skala": "Kategori (Nominal)",
                "alasan": f"Jawaban mengandung kategori '{kata}'."
            }

    return {
        "jenis_data": "Kualitatif",
        "skala": "Nominal",
        "tipe_skala": "Teks Bebas (Nominal)",
        "alasan": "Jawaban berbentuk label/kategori tanpa urutan."
    }

# -----------------------
# rekomendasi grafik
# -----------------------
def rekomendasi_grafik(instrumen: str, contoh_jawaban: str, audiens: str = "siswa") -> list:
    jaw = str(contoh_jawaban or "").lower()
    answers = [a.strip() for a in re.split(r"[,\n;]+", jaw) if a.strip()]

    num_count = len(re.findall(r"\d+(\.\d+)?", jaw))
    is_likert = any(p in jaw for p in likert_patterns)
    is_numeric = num_count >= max(1, len(answers)//2) if answers else False

    recs = []
    if is_likert:
        recs.append({
            "grafik": "Bar chart (frekuensi tiap tingkat)",
            "kenapa": "Skala Likert bersifat ordinal — tampilkan frekuensi tiap tingkat.",
            "kapan": "Saat ingin menunjukkan distribusi jawaban tingkat (mis. setuju/tidak).",
            "saran_presentasi": "Tampilkan proporsi (%) dan jumlah, beri label jelas."
        })
        recs.append({
            "grafik": "Stacked bar",
            "kenapa": "Membandingkan distribusi Likert antar kelompok.",
            "kapan": "Jika ada beberapa kelompok audiens.",
            "saran_presentasi": "Gunakan warna kontras untuk tiap tingkat."
        })
    elif is_numeric:
        recs.append({
            "grafik": "Histogram",
            "kenapa": "Menunjukkan distribusi nilai numerik (sebaran).",
            "kapan": "Data kuantitatif kontinu atau banyak variasi nilai.",
            "saran_presentasi": "Tampilkan bin yang sesuai dan label frekuensi."
        })
        recs.append({
            "grafik": "Boxplot",
            "kenapa": "Menampilkan median, kuartil, dan pencilan (outlier).",
            "kapan": "Untuk ringkasan lima angka (min, Q1, median, Q3, max).",
            "saran_presentasi": "Sertakan median dan keterangan outlier."
        })
    else:
        recs.append({
            "grafik": "Bar chart (kategori)",
            "kenapa": "Nominal lebih mudah dibaca dengan batang per kategori.",
            "kapan": "Jawaban berupa label/kategori.",
            "saran_presentasi": "Urutkan kategori dari frekuensi tertinggi."
        })
        recs.append({
            "grafik": "Pie chart (proporsi)",
            "kenapa": "Menampilkan komposisi; gunakan jika kategori sedikit.",
            "kapan": "Jumlah kategori ≤ 6.",
            "saran_presentasi": "Tampilkan persentase dan hindari terlalu banyak slice."
        })

    for r in recs:
        if audiens.lower() == "siswa":
            r["saran_presentasi"] = r["saran_presentasi"] + " (sederhana, label besar)"
        else:
            r["saran_presentasi"] = r["saran_presentasi"] + " (tambahkan ringkasan statistik jika perlu)"
    return recs

# -----------------------
# generate PDF
# -----------------------
def generate_pdf_for_group(group_meta: dict, lkm_answers: dict) -> bytes:
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4
    left = 2 * cm
    top = height - 2 * cm

    c.setFont("Helvetica-Bold", 16)
    c.drawString(left, top, "DATA HEROES — LKM Statistik Digital")
    c.setFont("Helvetica", 9)
    c.drawString(left, top - 16, f"Generated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}")
    c.line(left, top - 18, width - left, top - 18)

    y = top - 36
    c.setFont("Helvetica-Bold", 12)
    c.drawString(left, y, f"Kelompok {group_meta.get('Kelompok','')}: {group_meta.get('Nama Kelompok','')}")
    y -= 14
    c.setFont("Helvetica", 10)
    c.drawString(left, y, f"Kelas: {group_meta.get('Kelas','')}")
    y -= 12
    c.drawString(left, y, "Anggota:")
    y -= 12
    for anggota in str(group_meta.get('Anggota','')).splitlines():
        c.drawString(left + 8, y, f"- {anggota}")
        y -= 12
        if y < 3 * cm:
            c.showPage()
            y = top

    for pertemuan, answers in (lkm_answers or {}).items():
        if y < 4 * cm:
            c.showPage()
            y = top
        c.setFont("Helvetica-Bold", 11)
        c.drawString(left, y, pertemuan)
        y -= 14
        c.setFont("Helvetica", 10)
        if isinstance(answers, dict):
            for k, v in answers.items():
                text = f"{k}: {v}"
                while len(text) > 120:
                    c.drawString(left + 6, y, text[:120])
                    text = text[120:]
                    y -= 12
                    if y < 3 * cm:
                        c.showPage()
                        y = top
                c.drawString(left + 6, y, text)
                y -= 12
        else:
            c.drawString(left + 6, y, str(answers))
            y -= 12
        y -= 8

    c.showPage()
    c.save()
    buffer.seek(0)
    return buffer.read()
