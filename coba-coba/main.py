import os
import subprocess

def cek_release():
  try:
    result = subprocess.run(["cat", "/etc/os-release"], capture_output=True, text=True, check=True)
    print("Ini adalah informasi sistem")
    print(result.stdout)
  except subprocess.CalledProcessError as e:
    print(f"Error menjalankan apt update: {e}")
    print(e.stderr)

def update_script():
    """Menjalankan script update.sh."""
    try:
        subprocess.run(["sh", "update.sh"], check=True)
        print("Script update.sh berhasil dijalankan.")
    except subprocess.CalledProcessError as e:
        print(f"Error menjalankan script update.sh: {e}")
    except FileNotFoundError:
        print("File update.sh tidak ditemukan.")

def upgrade_script():
    """Contoh fungsi lain."""
    try:
        subprocess.run(["sh", "upgrade.sh"], check=True)
        print("Script upgrade berhasil dijalankan")
    except subprocess.CalledProcessError as e:
        print(f"Script Error, {e}")
    except FileNotFoundError:
        print("file upgrade.sh tidak ditemukan/Cek permission")

def fungsi_ketiga():
    """Contoh fungsi ketiga."""
    print("Fungsi ketiga dijalankan.")

def main():
    """Fungsi utama untuk memilih fungsi."""
    print("Daily Linux system maintenance")
    print("works on ubuntu/Debian based")
    print("Pilih fungsi:")
    print("1. Jalankan update.sh")
    print("2. Jalankan Upgrade.sh")
    print("3. Jalankan fungsi ketiga")
    cek_release()
    pilihan = input("Masukkan nomor pilihan: ")

    if pilihan == "1":
        update_script()
    if pilihan == "2":
        upgrade_script()
    if pilihan == "3":
        fungsi_ketiga()
    else:
        print("Jalankan ulang script untuk pilihan lainnya")

if __name__ == "__main__":
    main()