def tambah (x,y):
    return x + y

def kurang (x,y):
    return x - y

def kali (x,y):
    return x * y

def bagi (x,y):
    if y == 0:
        return "Error: Pembagian tidak boleh dengan nol!"
    return x / y

def kalkulator():
    while True:
        print("Selamat Datang")
        print("Pilih Operasi:")
        print("1. Tambah")
        print("2. Kurang")
        print("3. Kali")
        print("4. Bagi")

        operasi = input("Pilih Operasi atau q untuk keluar: ")

        if operasi == 'q':
            print("Terimakasih :)")
            break

        if operasi not in [ '1','2','3','4']:
            print("Pilihan Tidak Valid, Ulangi")
            continue
        
        try:
            angka1 = float(input("Masukkan angka pertama: "))
            angka2 = float(input("Masukkan angka kedua: "))
        except ValueError:
            print("Input yang dimasukkan tidak valid, Harap Masukkan angka.")
            continue
        
        if operasi == '1':
            print(f"Hasil: {angka1} + {angka2} = {tambah(angka1,angka2)}")
            break
        elif operasi == '2':
            print(f"Hasil {angka1} - {angka2} = {kurang(angka1,angka2)}")
            break
        elif operasi == '3':
            print(f"Hasil {angka1} * {angka2} = {kali(angka1,angka2)}")
            break
        elif operasi == '4':
            print(f"Hasil {angka1} / {angka2} = {bagi(angka1,angka2)}")
            break


        
kalkulator()
