"""UTS Dasar Komputer dan Pemrograman - Kelompok E."""

DATA_KELEMBAPAN = [
    22, 28, 34, 41, 55, 63, 72, 78, 31, 47,
    66, 81, 19, 58, 69, 34, 35, 70, 71, 90,
]
KATEGORI = ("KERING", "NORMAL", "BASAH")


def status_sensor(nilai):
    """Kembalikan kategori untuk kelembapan dalam persen."""
    if nilai < 35:
        return "KERING"
    elif nilai <= 70:
        return "NORMAL"
    else:
        return "BASAH"


def aksi_pompa(status):
    """Nyalakan pompa hanya untuk kondisi KERING."""
    if status == "KERING":
        return "ON"
    return "OFF"


def rata_rata(data):
    """Hitung rata-rata nilai kelembapan."""
    return sum(data) / len(data)


def hitung_kategori(data):
    """Hitung jumlah data untuk setiap kategori."""
    jumlah = {kategori: 0 for kategori in KATEGORI}
    for nilai in data:
        jumlah[status_sensor(nilai)] += 1
    return jumlah


def main():
    print("===== MONITORING KELEMBAPAN TANAH =====")
    for nomor, nilai in enumerate(DATA_KELEMBAPAN, start=1):
        status = status_sensor(nilai)
        print(f"{nomor:02d}. Kelembapan: {nilai:>3}% | {status:<6} | Pompa: {aksi_pompa(status)}")

    jumlah = hitung_kategori(DATA_KELEMBAPAN)
    print("\n===== RINGKASAN =====")
    print(f"Total data      : {len(DATA_KELEMBAPAN)}")
    for kategori in KATEGORI:
        print(f"{kategori:<15} : {jumlah[kategori]}")
    print(f"Rata-rata       : {rata_rata(DATA_KELEMBAPAN):.2f}%")
    print(f"Maksimum        : {max(DATA_KELEMBAPAN)}%")
    print(f"Minimum         : {min(DATA_KELEMBAPAN)}%")


if __name__ == "__main__":
    main()
