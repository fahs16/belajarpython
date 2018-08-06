print ("Bitwise Operator")
print ("""
	Operator bitwise digunakan untuk menangani operasi operasi bit pada suatu
	bilangan dalam representasi binner. Pastikan kamu sudah mengerti
	bilangan binner dan operasi gerbang logika dahulu yah. Biar gampang
	ngertiinnya. FYI, operasi gerbang logika biasanya ada di materi 
	sistem komputer. Jadi dalam menjalankan operasi bitwise, python akan
	mengubah data integer (decimal) kedalam binner terlebih dahulu, 
	kemudian dijalankan operasi bitwise yang telah ditentukan, 
	akhirnya hasil dari operasi bitwise yang semula bilangan binner,
	akan diubah kembali menjadi bilangan decimal. Makanya kalau tidak tahu
	bilangan binner bakalan susah mahaminnya.

Operator Bitwise dilambangkan dengan lambang berikut:

	&   | melambangkan operasi AND terhadap dua bilangan.
	|   | melambangkan operasi OR terhadap dua bilangan.
	^   | melambangkan operasi XOR terhadap dua bilangan.
	>>  | untuk melakukan operasi penggeseran bit ke kanan
	    | dalam bilangan binner.
	<<  | untuk melakukan operasi penggeseran bit ke kiri
	    | dalam bilangan binner.
	~   | untuk melakukan operasi negasi terhadap suatu bilangan.
	    | operasinya memiliki rumus -(n+1). Apabila kita melakukan
	    | operasi '(~6)' maka akan menghasilkan output '-7'

Disini saya menjelaskan secara singkat cara kerja operator bitwise diatas
dari nomor 1 sampai 5. Kalau yg nomor 6 saya rasa mudah dimengerti.

50  -> dikonversi ke biner menjadi 0011 0010
39  -> dikonversi ke biner menjadi 0010 0111

  A. Operasi Bitwise 'AND' (50 & 39)
input   0011 0010
input   0010 0111
        ---------  Apabila kedua input bernilai 1, maka output 1
output	0010 0010  (34)

  B. Operasi Bitwise 'OR" (50 | 39)
input   0011 0010
input	0010 0111
        ---------  Apabila ada input yang bernilai 1, maka output 1
output  0011 0111  (55)

  C. Operasi Bitwise 'XOR' (50 ^ 39)
input	0011 0010
input	0010 0111
        ---------  Apabila kedua input bernilai sama, maka output 0
output  0001 0101  (21)

  D. Operasi Bitwise Left Shift << (50 << 2)
input	0011 0010
        --------- misalnya kita akan menggeser bit ke kiri 2 '<< 2'
output	1100 1000 (200)

  E. Operasi Bitwise Right Shift >> (50 >> 2)
input	0011 0010
        ---------  misalnya kita akan menggeser bit ke kanan 2 '<< 2'
output	0000 1100  (12)

""")


print ("(50 & 39) =", 50 & 39)
print ("(50 | 39) =", 50 | 39)
print ("(50 ^ 39) =", 50 ^ 39)
print ("(50 << 2) =", 50 << 2)
print ("(50 >> 2) =", 50 >> 2)
print ("(~50) 	  =", ~50)
