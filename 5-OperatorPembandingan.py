print ("Comparison Operator")
print ("""
	Operator perbandingan biasa digunakan untuk penggunaan
	pemilihan kondisi dan perulangan.
	Operator perbandingan digunakan untuk membandingka
	dua buah variabel dan akan menghasilkan kondisi True dan False.
""")

print ("""Operator perbandingan pada python diantaranya adalah :

	==   |> sama denga
	     |  - Apabila nilai sebelah kiri dan sebelah kanan sama, 
	     |    maka akan menghasilkan kondisi True.
	!=   |> tidak sama dengan
	     |  - Apabila nilai sebelah kiri dan sebelah kanan sama, 
	     |    maka akan menghasilkan kondisi False.
	     |  - Apabila nilai sebelah kiri dan sebelah kanan beda, 
	     |    maka kan menghasilkan kondisi True
	>    |> lebih besar dari
	     |  - Apabila nilai sebelah kiri lebih besar dari sebelah kanan, 
	     |    maka akan menghasilkan kondisi True.
	<    |> kurang besar dari
	     |  - Apabila nilai sebelah kiri lebih kecil dari sebelah kanan,
	     |    maka akan menghasilkan kondisi True.
	>=   |> lebih dari atau sama dengan
	     |  - Apabila nilai sebelah kiri lebih besar dari sebelah kanan, 
	     |    atau sama kedua nilainya, maka akan menghasilkan kondisi True.
	<=   |> kurang dari atau sama dengan
	     |  - Apabila nilai sebelah kiri lebih kecil dari sebelah kanan, 
	     |    atau sama kedua nilainya, maka akan menghasilkan kondisi True.
""")

print ("Contoh penggunaan operator perbandingan : ")
print ("""Kita akan menggunakan dua buah variabel sebagai berikut :

	a = 22
	b = 90
	c = 22
""")

a = 22
b = 90
c = 22

print ("""A. Operator Sama Dengan '=='
	a == b""", a == b, """
	a == c""", a == c)

print ("""B. Operator Tidak Sama Dengan '!='
	a != b""", a != b, """
	a != c""", a != c)

print ("""C. Operator Lebih Besar '>'
	a > b""", a > b, """
	b > a""", b > a)

print ("""D. Operator Kurang Besar '<'
	a < b""", a < b, """
	b < a""", b < a)

print ("""E. Operator Lebih Besar atau Sama Dengan '>='
	a >= b""", a >= b, """
	a >= c""", a >= c, """
	b >= c""", b >= c)

print ("""F. Operator Kurang Besar atau Sama Dengan '<='
	a <= b""", a <= b, """
	a <= c""", a <= c, """
	b <= c""", b <= c)
