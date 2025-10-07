judul = "Praktikum Pemprograman Dasar Python 2 - Variable dan Tipe data" 
a = False
print(a)        #Ini adalah boolean
print(type(a))

teks_string = "Ini adalah tulisan berupa String" # ini adalah string
print(teks_string)

value_1 = 100 #ini adalah interger
print(value_1)

value_2 = 0.001 # Ini adalah float
print(value_2)


var_1 = 0x01 # ini adalah variabel pertama dengan data hexa
var_2 = var_1 # ini adalah variable kedua dengan data interger
#print(var_2)
print("Bilangan desimal dari 0x01 adalah", var_2)

# bilangan complex
complex_mentah = 10 + 0j # bilangan kompleks sebelum dikonversi
complex_dadi = complex_mentah.real #konversi bilangan complex ke rill murni
print(int(complex_dadi)) #print dengan format interger
print(type(complex_mentah))

complex_mentah_2 = 2 + 6j
print(complex_mentah_2)
print(type(complex_mentah_2))

# Tipe data set
data_set = {96, 97, 98, 99, 100}
print(data_set)

data_set_2 = {'seratus', 'dua ratus', 'tiga ratus',}
print(data_set_2)

# Data Dictionary
data_dictionary = {'nama':'Ani', 'umur': 19}
print(data_dictionary)

print("This strings contains a single quote (') character.")