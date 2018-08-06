print ("Arithmethic Operator")
print ("""
	Pada kali ini kita akan mempelajari tentang operasi aritmatika di python.
	Mulai dari perkalian, pertambahan, dan sejenisnya. 
	Operator aritmatika yang akan dibahas pada bab ini levelnya masih dasar yah.
	Cuma sekedar perhitungan biasa.
""")
print ("""Operator aritmatika dasar pada python :

	+  > pertambahan (hanya operator pertambahan yang bisa melakukan operasi
	     dengan value tipedata string)
	-  > pengurangan
	*  > perkalian (bisa digunakan antara tipe data string dan integer)
	/  > pembagian
	%  > modulus
	** > perpangkatan
	// > pembagian bulat (hasil pembagian akan dibulatkan, jadi hasilnya
	     tidak ada komanya.)

""")

print ("""Pada pembahasan ini, saya akan menggunakan beberapa variabel berikut :
	a = 16
	b = 9
	A = "a"
	B = "b"
""")
a = 16
b = 9
A = "a"
B = "b"

print ("Contoh Hasil Operasi Aritmatika :")
hasil = a + b
print ("a + b	=", hasil)
hasil = A + B
print ("A + B	=", hasil)
hasil = a - b
print ("a - b	=", hasil)
hasil = a * b
print ("a * b	=", hasil)
hasil = A * b
print ("A * b	=", hasil)
hasil = b * B
print ("b * B	=", hasil)
hasil = a / b
print ("a / b	=", hasil)
hasil = a ** b
print ("a ** b	=", hasil)
hasil = a // b
print ("a // b	=", hasil)
hasil = a % b
print ("a % b	=", hasil)

