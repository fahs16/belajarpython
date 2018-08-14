print("""TUPLE

	Tuple adalah tipe data majemuk seperti list
	yang isi dari data ini tidak dapat diubah.
	namun ada cara agar tipe data tuple ini
	dapat dirubah. caranya adalah dengan 
	mengubah data tuple ini ke list dahulu.

	Cara mengubah tipe data tuple ke list :
	x = ("a","b","c","d",5)
	print(x)
	y = list(x)
	y.append("z")
	x = tuple(y)
	print(x)
""")
x = ("a","b","c","d",5)
print(x)
y = list(x)
y.append("z")
x = tuple(y)
print(x)
print("""
Sedangkan, untuk mengakses tuple, kita bisa
menggunakan metode index dan count

print(x.count(5))
print(x.index(4))
""")
print(x.count(5))
print.(x.index(4))
