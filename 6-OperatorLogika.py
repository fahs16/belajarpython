print ("Logical Operator")
print("""
	Sama seperti operator perbandingan sebelumnya, operator ini akan
	menghasilkan value berupa True dan False. Operator logika ini
	biasanya digunakan dalam pemilihan kondisi seperti while atau for.
	Penggunaannya bisa digabung dengan operator perbandingan.
	Kalau anda sudah mengerti tentang gerbang logika, pastinya anda
	mudah memahaminya.
""")

print ("""Ada beberapa operator logika di python, diantaranya:

	and  | Ketika kondisi suatu operator akan menghasilkan True,
	     | dan ketika ditambahkan operasi logika dengan 'and'
	     | maka hasilnya akan tetap True.
	or   | Ketika kondisi suatu operator akan menghasilkan False,
	     | dan ketika ditambahkan operasi logika dengan 'or'
	     | maka akan menghasilkan False.
	not  | Kondisi ini merupakan operasi kebalikan. Ketika nilai
	     | suatu variabel True, maka akan diubah menjadi False.
	     | Operator ini akan mengubah suatu data boolean menjadi
	     | kebalikan dari data tersebut.
""")

print ("""Untuk memulai operasi logika, kita akan menggunakan 2 variabel:
	a = "aku"
	b = "kamu"
Contoh: """)

a = "aku"
b = "kamu"

print ("a == b", a == b)
print ("a != b", a != b)
print ("(a == b and a != b)", (a == b and a != b) )
print ("(a == b or a != b)", (a == b or a != b) )
print ("not(a == b)", not(a == b) )
