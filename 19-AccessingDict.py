x = {
	"merah" : "saus",
	"pedas" : "cabe",
	"manis" : {
		"putih" : "gula",
		"hitam" : "dodol",
		"kuning" : {
			"buah" : "pisang",
			"agar" : "mangga",
		},
	},
	"es" : "dingin"
}

print("""Mengakses Dictionary

	Lebih jelasnya, jalankan file ini dan
	lihat sesuai sesuai pemanggilannya
""")

print("""

Dictionarynya :

x = {
	"merah" : "saus",
	"pedas" : "cabe",
	"manis" : {
		"putih" : "gula",
		"hitam" : "dodol",
		"kuning" : {
			"buah" : "pisang",
			"agar" : "mangga",
		},
	},
	"es" : "dingin"
}
""")
print("print(x)")
print(x)
print("""
print(x["merah"])
""")
print(x["merah"])
print("""
print(x["pedas"])
""")
print(x["pedas"])
print("""
print(x["manis"])
""")
print(x["manis"])
print("""
print(x["manis"]["putih"])
""")
print(x["manis"]["putih"])
print("""
print(x["manis"]["kuning"])
""")
print(x["manis"]["kuning"])
print("""
print(x["manis"]["kuning"]["buah"])
""")
print(x["manis"]["kuning"]["buah"])
