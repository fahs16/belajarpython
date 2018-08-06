print("Elif Statement")
print("""
	Elif statement memungkinkan kita membuat kondisional lebih dari 1,
	sebelumnya kita tau if dan else. Dengan adanya elif, kita dapat
	membuat banyak kondisi dengan banyak reaksinya.

rumus penggunaan :

	if 'kondisi A':
		'reaksi A'
	elif 'kondisi B':
		'reaksi B'
	elif 'kondisi C':
		'reaksi C'
	else:
		'reaksi Z'

  *Catatan : dengan elif, kamu bisa mengakhiri sebuah kondisi
	     dengan atau tanpa else.

variabel lab ini:

	nilai = 65
""")

nilai = 65

if nilai >= 96:
	print ("Kamu Genius!")
elif nilai >= 80 and nilai < 96:
	print ("Kamu Pintar!")
elif nilai >= 70 and nilai < 80:
	print ("Belajar lagi, kamu pasti bisa")
elif nilai >=65 and nilai <=70:
	print ("Jangan main melulu")
else:
	print ("goblok lu!")
