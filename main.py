a = 10
b = 20
c = 5
d = 8
e = 12

tambah = a + b + c + d + e
rata_rata = tambah / 5

Angka = [a, b, c, d, e]
nilai_max = max(Angka)
nilai_min = min(Angka)
hasil_perkalian = a * b * c * d * e
selisih = nilai_max - nilai_min

print("Angka = ", a, b, c, d, e)
print("jumlah = ", tambah)
print("Rata-rata:", (rata_rata))
print("Selisih max-min = ", selisih)
print("Hasil Perkalian:", hasil_perkalian)


# Konversi bilangan desimal ke biner python
desimal_a = 12
desimal_b = 5

# Konversi desimal ke biner menggunakkan fungsi bin di python3
biner_a = bin(desimal_a)
biner_b = bin(desimal_b)

# Penggunaan operator & | ^
operator_and_desimal = desimal_a & desimal_b
operator_and_biner = bin(operator_and_desimal)
operator_or_desimal = desimal_a | desimal_b
operator_or_biner = bin(operator_or_desimal)
operator_xor_desimal = desimal_a ^ desimal_b
operator_xor_biner = bin(operator_xor_desimal)
operator_not_desimal = ~a
operator_not_biner = bin(operator_not_desimal)
operator_left_shift_desimal = desimal_a << 1
operator_left_shift_biner = bin(operator_left_shift_desimal)
operator_right_shift_desimal = desimal_b >> 2
operator_right_shift_biner = bin(operator_right_shift_desimal)

# Operasi Bitwise
output_1 = f"a={desimal_a} ({biner_a}), b={desimal_b} ({biner_b})"
output_2 = f"a & b = {operator_and_desimal} ({operator_and_biner})"
output_3 = f"a | b = {operator_or_desimal} ({operator_or_biner})"
output_4 = f"a ^ b = {operator_xor_desimal} ({operator_xor_biner})"
output_5 = f"~a = {operator_not_desimal} ({operator_not_biner}) (biner tergantung sistem)"
output_6 = f"{desimal_a} << 1 = {operator_left_shift_desimal} ({operator_left_shift_biner})"
output_7 = f"{desimal_b} >> 2 = {operator_right_shift_desimal} ({operator_right_shift_biner})"

print(output_1)
print(output_2)
print(output_3)
print(output_4)
print(output_5)
print(output_6)
print(output_7)