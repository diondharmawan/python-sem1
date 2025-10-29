def hitung_harga_akhir(total_belanja):
    """
    Menghitung harga akhir setelah diskon berdasarkan total belanja.

    Args:
        total_belanja (float): Total belanja pelanggan.

    Returns:
        float: Harga akhir setelah diskon.
    """

    diskon = 0.0

    if total_belanja > 500000:
        diskon = 0.20  # 20% diskon
    elif total_belanja > 200000:
        diskon = 0.10  # 10% diskon
    elif total_belanja > 50000:
        diskon = 0.05  # 5% diskon
    #Tidak perlu kondisi else, diskon sudah diinisialisasi 0

    harga_akhir = total_belanja * (1 - diskon)
    return harga_akhir


# Input dari pengguna
total_belanja = float(input("Masukkan total belanja: Rp"))

# Hitung dan tampilkan harga akhir
harga_akhir = hitung_harga_akhir(total_belanja)
print(f"Total belanja: Rp{total_belanja:,.0f}")
print(f"Harga akhir setelah diskon: Rp{harga_akhir:,.0f}")