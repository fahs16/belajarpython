print ("Type Conversion")
print ("""
	Pada kali ini kita akan belajar tentang Type Conversion.
	Tujuannya adalah untuk mengkonversi suatu tipe data python kedalam
	tipe data lainnya. Untuk mengkonversi tipe data, kita akan menggunakan
	beberapa function berikut. 
""")

print ("""
chr()		= untuk mengubah angka (integer) ke karakter.
		  kalau kita mengubah tipedata string, maka akan terjadi eror.
unichr()	= untuk mengubah angka (integer) ke karakter unicode.
		  fungsi ini hanya bisa digunakan pada python2.
		  kalau kita mengubah tipedata string, maka akan terjadi eror.
str()		= untuk mengubah value variabel angka atau huruf ke string.
complex()	= untuk mengubah angka ke bilangan complex.
		  kalau kita mengubah tipedata string, maka akan terjadi eror.
float()		= untuk mengubah angka ke bilangan koma
hex()		= untuk mengubah angka ke bilangan hexadecimal
oct()		= untuk mengubah angka ke bilangan octal
int()		= untuk mengubah tipedata lain ke angka

Pertama kita akan membuat sebuah variabel sebagai berikut:
bil = 200
huruf = "kata"
""")


bil = 200
huruf = "kata"

var1 = chr(bil)
var2 = str(bil)
var3 = str(huruf)
var4 = complex(bil)
var5 = float(bil)
var6 = hex(bil)
var7 = oct(bil)
var8 = int(bil)

print (var1)
type(var1)
print (var2)
type(var2)
print (var3)
type(var3)
print (var4)
type(var4)
print (var5)
type(var5)
print (var6)
type(var6)
print (var7)
type(var7)
print (var8)
type(var8)
