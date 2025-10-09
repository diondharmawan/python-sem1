import os
import subprocess

def update_script():
    """Menjalankan script update.sh."""
    try:
        subprocess.run(["sh", "update.sh"], check=True)
        print("Script update.sh berhasil dijalankan.")
    except subprocess.CalledProcessError as e:
        print(f"Error menjalankan script update.sh: {e}")
    except FileNotFoundError:
        print("File update.sh tidak ditemukan.")

def fungsi_lain():
    """Contoh fungsi lain."""
    try:
        subprocess.run(["sh", "upgrade.sh"], check=True)
        pri

def fungsi_ketiga():
    """Contoh fungsi ketiga."""
    print("Fungsi ketiga dijalankan.")

def main():
    """Fungsi utama untuk memilih fungsi."""
    print("Pilih fungsi:")
    print("1. Jalankan update.sh")
    print("2. Jalankan fungsi lain")
    print("3. Jalankan fungsi ketiga")

    pilihan = input("Masukkan nomor pilihan: ")

    if pilihan == "1":
        update_script()
    elif pilihan == "2":
        fungsi_lain()
    elif pilihan == "3":
        fungsi_ketiga()
    else:
        print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()