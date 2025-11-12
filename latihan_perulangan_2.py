# Program Deret Bilangan
# Jika i ganjil → i^2
# Jika i genap → i * 2

# Input jumlah suku
N = int(input("Masukkan N: "))

total = 0
deret = []

# Loop untuk menghasilkan deret
for i in range(1, N + 1):
    if i % 2 == 1:      # suku ganjil
        nilai = i ** 2
    else:               # suku genap
        nilai = i * 2
    deret.append(nilai)
    total += nilai

# Tampilkan deret
for nilai in deret:
    print(nilai, end=" ")

# Tampilkan total
print("\nTotal =", total)
