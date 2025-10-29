def hitung_gaji(jabatan, jam_kerja):
    """
    Menghitung gaji berdasarkan jabatan dan jam kerja (hanya menggunakan if dan input di depan).

    Args:
        jabatan (str): Jabatan karyawan (Manager, Supervisor, Staff).
        jam_kerja (int): Jumlah jam kerja karyawan.

    Returns:
        float: Total gaji yang diterima karyawan.
    """

    tarif_manager = 100000
    tarif_supervisor = 75000
    tarif_staff = 50000

    # Tarif awal dikondisikan dengan 0 agar tidak terisi dengan bilangan lain sebelum diiisi dengan variabel jam_kerja
    tarif = 0
    if jabatan == "Manager":
        tarif = tarif_manager
    if jabatan == "Supervisor":
        tarif = tarif_supervisor
    if jabatan == "Staff":
        tarif = tarif_staff

    if tarif == 0:
        return "Jabatan tidak valid."

    jam_normal = 0
    if jam_kerja > 8:
      jam_normal = 8
    else:
      jam_normal = jam_kerja


    jam_lembur = 0
    if jam_kerja > 8:
        jam_lembur = jam_kerja - 8
    else:
      jam_lembur = 0

    gaji_normal = jam_normal * tarif
    gaji_lembur = jam_lembur * tarif * 1.5

    total_gaji = gaji_normal + gaji_lembur
    return total_gaji


# Input dari pengguna
jabatan = input("Masukkan jabatan (Manager, Supervisor, Staff): ")
print("case sensitive, pastikan input sampeyan sesuai dengan Value yang diminta")
jam_kerja = int(input("Masukkan jumlah jam kerja: "))

# Hitung dan tampilkan gaji
gaji = hitung_gaji(jabatan, jam_kerja)

if isinstance(gaji, str):  # Check if the return value is an error message
    print(gaji)
else:
    print(f"Gaji {jabatan}: Rp{gaji:,.0f}")