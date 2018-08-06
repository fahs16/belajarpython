print ("Nested If")
print ("""
	Terkadang kita harus menyelesaikan 2 kondisi untuk menggapai
	tujuan kita.  Misalnya, buat
	mendapatkan bakso sesuai selera kita, kita ditanyain mau pake
	sambel atau ngga, kalau kita jawab pake, abangnya pasti tanya
	lagi pedes apa sedeng. Nah itulah contohnya dalam kehidupan
	sehari hari. Bahasa kerennya disini 'Nested If'.

	Kalau kondisi pertama terpenuhi, kondisi didalamnya akan
	diperiksa dan bila kondisi di dalam kondisi pertama terpenuhi,
	maka kode akan dieksekusi.

variabel lab :
	nilai = 95
""")

nilai = 100

if nilai > 75:
	print ("Selamat kamu lulus ujian!")
	if nilai <= 100 and nilai >= 99 :
		print ("Selamat kamu dapat gratis SPP 1 Bulan")
		if nilai == 100:
			print ("Selamat kamu dapat beasiswa")
	elif nilai > 95 and nilai <= 98 :
		print ("Selamat kamu dapat voucher jajan di kantin")
elif nilai <=75:
	print ("Kamu gak lulus ujian, silahkan remedial")
