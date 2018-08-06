print ("Identity Operator")
print ("""
	Operator identitas adalah cara bagaimana mengenali suatu variabel
	didalam memori di Python. Kita dapat membandingkan isinya apakah
	isinya identik ataupun lokasi memorinya.
Operator ini hanya ada dua :

	is	| untuk memeriksa apakah dua variabel memiliki isi dan
		| tipe data yang sama. apabila hasilnya sama, maka
		| akan menghasilkan output True
	is not	| untuk memeriksa dua variabel memiliki isi dan tipe data
		| yang berbeda. Apabila hasilnya kedua variabel berbeda
		| maka akan menghasilkan output True

  *Catatan : apabila agan mencoba mennggunakan 'is' pada 2 variabel yang
	     menggunakan tipe data list, dict, dan tuple, meskipun isi 
	     pada variabel sama entah mengapa akan menghasilkan False.
	     Kecuali kalau isi pada 2 variabel samasama berjenis tuple
	     namun hanya satu isi nilainya, maka akan menghasilkan True
	     untuk lebih jelasnya, silahkan coba sendiri :)

Ada function yang bisa dugunakan untuk operator ini :

	id()	| untuk mengetahui lokasi variabel / objek di memori
		| walaupun isi dan tipe datanya sama.

rumus dasarnya :
	'var1' is 'var2
	'var1' is not 'var2'
	id(var1) is id(var2)
	id(var1) is not id(var2)

untuk pengujiannya, disini saya akan membuat variabel sebagai berikut :

anggota = [ "ali", "aisyah", "rara", "ploy" ]
anggota_copy = [ "ali", "aisyah", "rara", "ploy" ]
member = ( "ali", "aisyah", "rara", "ploy" )
a = 1
b = 1
""")

anggota = [ "ali", "aisyah", "rara", "ploy" ]
anggota_copy = [ "ali", "aisyah", "rara", "ploy" ]
member = ( "ali", "aisyah", "rara", "ploy" )
a = 1
b = 1
c = "1"

print ("(anggota is member) =",(anggota is member))
print ("(anggota is anggota_copy) =", (anggota is anggota_copy))
print ("(anggota is not member) =", (anggota is not member))
print ("(anggota is not anggota_copy) =",(anggota is not anggota_copy))
print ("(id(anggota) is id(anggota)) =", (id(anggota) is id(anggota)))
print ("(id(anggota) is not id(member)) =", (id(anggota) is not id(member)))
print ("(id(anggota) is id(anggota_copy)) =", (id(anggota) is id(anggota_copy)))
print ("(id(member) is id(member)) =", (id(member) is id(member)))
print ("(a is b) =", (a is b))
print ("(a is c) =", (a is c))
