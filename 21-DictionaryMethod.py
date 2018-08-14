print("""
Dictionary Method

	Untuk bermain dengan dictionary, ada beberapa method
	yang bisa digunakan. diantaranya :
	1. get : untuk mengambil value dari suatu key
	2. has_key : untuk memeriksa apakah data dictionary 
			memiliki key atau ngga.
	3. keys : untuk mengambil keynya saja.
	4. items : untuk mengambil valuenya saja.
	5. update : untuk menambah isi dict
	6. pop : untuk membuag salah satu elemen
	7. popitem : untuk membuang satu elemen dari depan
	8. clear : untuk menghapus semua elemen
""")
#var :
d = {"siang" : "zuhur", "pagi": "subuh", "sore":"ashar", "petang":"maghrib","malam":"isya", "zikir": " "}
e = {"midnight": "tahajud"}

print(d.get("malam"))
print(d.has_key("siang"))
print(d.has_key("zikir"))
print(d.keys())
print(d.items())
d.update(e)
print(d)
d.popitem()
print(d)
e.clear()
print(e)
