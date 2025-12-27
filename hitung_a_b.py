def pangkat(a, b):
    if b == 0:          # base case
        return 1
    else:               # recursive case
        return a * pangkat(a, b - 1)

a = int(input("Masukkan nilai a: "))
b = int(input("Masukkan nilai b: "))
print(a, "^", b, "=", pangkat(a, b))
