print ("If Statement")
print ("""
	Dalam algoritma kita mengenal pilihan. Untuk mewujudkan pilihan atau
	bisa juga kondisional kita akan menggunakan if. Cara kerjanya,
	kita harus tetapkan dulu suatu kondisi A yang akan melaksanakan 
	perintah A, dan kalau tidak memenuhi kondisi A, maka akan melakukan
	perintah yang lainnya.
	Statement if memerlukan kondisi yang dibuat dengan operator logika
	dan operator relasional. Kemudian kalau kondisi itu tidak sesuai,
	maka else yang akan melanjutkannya.

rumus penggunaan:
	if 'kondisi A':
		'reaksi A'
	else:
		'reaksi B'
  * Catatan: Baris reaksi harus diberikan tab.

Variabel lab ini:
	nilai = 65
""")

nilai = 65

if nilai > 80:
	print ("Selamat, kamu lulus ujian.")
else:
	print ("Kamu belum lulus ujian.")

