import csv
import os.path


def satu():
    f = open('datanya.csv', 'r')
    reader = csv.reader(f)
    for row in enumerate(reader):
        print(row)
    f.close()

    

def dua():
    datanya = []
    nama = input("Masukkan Nama : ")
    pacar = input("Masukkan Nama Pasangan Kamu : ")
    
    if os.path.isfile('datanya.csv'):
        with open('datanya.csv', 'r+', newline='') as f:

            reader = csv.reader(f)
            
            for row in reader:
                row.append(datanya)
            inputan = []
            inputan.append(nama)
            inputan.append(pacar)
            datanya.append(inputan)
            w = csv.writer(f)

            for s in datanya:
                w.writerow(s)
            f.close()
    else:
        with open('datanya.csv', 'w', newline='') as f:

            inputan = []
            inputan.append(nama)
            inputan.append(pacar)
            datanya.append(inputan)
            w = csv.writer(f)
            w.writerow(('Nama', 'Pasangan'))

            for s in datanya:
                w.writerow(s)
            f.close()

def tiga():

    datanya = []
    input_baru = []

    with open('datanya.csv', 'r+', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            datanya.append(row)
        f.close()
    with open('datanya.csv', 'r+', newline='') as g:
        reader = csv.reader(g)
        for row in enumerate(reader):
            print(row)
        g.close()

        pilihan = int(input("Masukkan Urutan Nama : "))
        if pilihan == 0:
            print("Tidak bisa mengubah Judul")
            home()

        nama_baru = input("Masukkan Nama : ")
        pasangan_baru = input("Masukkan Pasangan : ")
        input_baru.append(nama_baru)
        input_baru.append(pasangan_baru)
        datanya.pop(pilihan)
        datanya.insert(pilihan, input_baru)
    with open('datanya.csv', 'w+', newline='') as h:
        w = csv.writer(h)
        for s in datanya:
            w.writerow(s)
        h.close()

def empat():
    datanya = []
    with open('datanya.csv', 'r+', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            datanya.append(row)
        f.close()
    with open('datanya.csv', 'r+', newline='') as g:
        reader = csv.reader(g)
        for row in enumerate(reader):
            print(row)
        g.close()
        pilihan = int(input("Masukkan Urutan Nama : "))
        if pilihan == 0:
            print("Tidak bisa menghapus judul")
            home()

        datanya.pop(pilihan)
    with open('datanya.csv', 'w+', newline='') as h:
        w = csv.writer(h)
        for s in datanya:
            print(s)
            w.writerow(s)
        h.close()





def home():
    menu = ("""
----------- MENU ----------
[1] Show Data
[2] Insert Data
[3] Edit Data
[4] Delete Data
[5] Exit
""")
    print(menu)
    pilihan = int(input("Pilihan Kamu > "))
    if pilihan == 1:
        satu()
    elif pilihan == 2:
        dua()
    elif pilihan == 3:
        tiga()
    elif pilihan == 4:
        empat()
    elif pilihan == 5:
        exit()
    else:
        print("Masukkan pilihan yang sesuai [1-5]")
    
while True:
    try:
        home()
    except FileNotFoundError:
        print("BELUM ADA DATA")
    except ValueError:
        print("MASUKKAN INPUT YANG SESUAI")
    