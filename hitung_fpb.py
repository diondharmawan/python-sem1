def fpb(a, b):
    if b == 0:          # base case
        return a
    else:               # recursive case
        return fpb(b, a % b)

x = int(input("Masukkan bilangan pertama: "))
y = int(input("Masukkan bilangan kedua: "))
print("FPB dari", x, "dan", y, "adalah", fpb(x, y))
