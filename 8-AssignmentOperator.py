print ("Assignment Operator")

print ("""
	Operator assignment digunakan ketika kita ingin melakukan sesuatu 
	terhadap sebuah variabel tanpa harus membuat variabel baru sebagai 
	variabel bantu. Ini bertujuan untuk menghemat baris kode.

Operator assignment pada python diantaranya:

	+=  | Untuk melakukan operasi pertambahan terhadap variabel.
	-=  | untuk melakukan operasi pengurangan terhadap variabel.
	*=  | untuk melakukan operasi perkalian terhadap variabel.
	/=  | untuk melakukan operasi pembagian terhadap variabel.
	%=  | untuk melakukan operasi modulus terhadap variabel.
	**= | untuk melakukan operasi pangkat terhadap variabel.
	//= | untuk melakukan operasi permbagian bulat terhadap variabel.

Untuk prakteknya, kita akan membuat satu variabel sebagai berikut
	a = 66
""")
a = 66
a += 12
print ("a += 12 =", a)

a = 66
a -= 12
print ("a -= 12 =", a)

a = 66
a *= 12
print ("a *= 12 =", a)

a = 66
a /= 12
print ("a /= 12 =", a)

a = 66
a %= 12
print ("a %= 12 =", a)

a = 66
a //= 12
print ("a //= 12 =", a)

a = 66
a **= 12
print ("a **= 12 =", a)

