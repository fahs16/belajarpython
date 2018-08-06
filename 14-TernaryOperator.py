print ("Ternary Operator")
print ("""
	Ternary Operator atau operator rangkap tiga ini adalah kondisional
	yang ditulis dengan lebih hemat. Tetapi struktur yang dapat dibuat
	hanya if dan else saja. Operator ini ditulis didalam variabel.

rumus :
	var1 = 'statement1' if 'kondisi' else 'statement2'
""")

total_belanja_A = 100000
diskon_A = "Selamat kamu dapat voucher belanja 20.000!" if total_belanja_A > 99000 else "Belanja lebih banyak untuk dapatkan voucher belanja"
total_belanja_B = 200000
diskon_B = "Selamat kamu dapat voucher belanja 20.000!" if total_belanja_B > 99000 else "Belanja lebih banyak untuk dapatkan voucher belanja"
total_belanja_C = 50000
diskon_C = "Selamat kamu dapat voucher belanja 20.000!" if total_belanja_C > 99000 else "Belanja lebih banyak untuk dapatkan voucher belanja"

print (diskon_A)
print (diskon_B)
print (diskon_C)
