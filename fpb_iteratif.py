def fpb_iteratif(a, b):
    while b != 0:
        sisa = a % b
        a = b
        b = sisa
    return a

x = int(input("Masukkan bilangan pertama: "))
y = int(input("Masukkan bilangan kedua: "))
print("FPB dari", x, "dan", y, "adalah", fpb_iteratif(x, y))
