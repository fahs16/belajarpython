print ("For Loop")

print ("""
	Loop atau perulangan berguna untuk melakukan tugas secra berulang.
	Pada python kita bisa menggunakan pengulangan dengan 'for ... in'
	Kemudian diikuti dengan function range() sebagai alat bantu untuk
	melakukan pengulangan dengan for range() memiliki tiga parameter
	awal, nilai akhir, dan penambah nilai untuk setiap iterasinya.

	Loop dengan for juga bisa memproses dengan data dengan tipe
	list, dict, tuple, atau string. Jadi ga perlu pake function range
	lagi.
""")

for i in range(1,5):
	print ("useradd bos{}".format(i))

for a in range(5,0,-1):
	print(a)


hewan = [ "anjing", "kambing", "kuda" ]
data = { "nama" : "kepo" , "umur" : 17 }
member = ("dono","fira","tri")
for tes in hewan:
	print ("binatang", tes)

for tes in data:
	print ("Yang harus dimasukkin :", tes)

for tes in member:
	print ("member {}".format(tes))

