# crack_simple.py

import re

# Input password dari pengguna
password = input("Masukkan password: ")

# Daftar alasan jika tidak valid
alasan = []

# 1. Panjang minimal 8 karakter
if len(password) < 8:
    alasan.append("- Panjang minimal 8 karakter")

# 2. Minimal 1 huruf besar
if not re.search(r"[A-Z]", password):
    alasan.append("- Minimal 1 huruf besar")

# 3. Minimal 1 huruf kecil
if not re.search(r"[a-z]", password):
    alasan.append("- Minimal 1 huruf kecil")

# 4. Minimal 1 angka
if not re.search(r"[0-9]", password):
    alasan.append("- Minimal 1 angka")

# 5. Minimal 1 karakter khusus dari !@#$%^&*
if not re.search(r"[!@#$%^&*]", password):
    alasan.append("- Minimal 1 karakter khusus")

# Output hasil validasi
if alasan:
    print("❌ Password tidak valid:")
    for a in alasan:
        print(a)
else:
    print("✅ Password valid")
