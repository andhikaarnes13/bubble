def urutasc(mylist) :
    mylist = sorted(mylist)
    print(mylist)

def urutdsc(mylist) :
    mylist = sorted(mylist, reverse=True)
    print(mylist)

print("Program Mengurutkan Data dengan metode Bubble sort")

angka1=int(input("Masukan Bilangan ke 1 : "))
angka2=int(input("Masukan Bilangan ke 2 : "))
angka3=int(input("Masukan Bilangan ke 3 : "))
angka4=int(input("Masukan Bilangan ke 4 : "))
angka5=int(input("Masukan Bilangan ke 5 : "))
angka6=int(input("Masukan Bilangan ke 6 : "))
angka7=int(input("Masukan Bilangan ke 7 : "))
angka8=int(input("Masukan Bilangan ke 8 : "))
angka9=int(input("Masukan Bilangan ke 9 : "))
angka10=int(input("Masukan Bilangan ke 10 : "))

angka=[angka1,angka2,angka3,angka4,angka5,angka6,angka7,angka8,angka9,angka10]

print("======================================")
print("Pilih Metode Pengurutan")
print("1. Sorting Ascending \n2. Sorting Descending")
pilih=input("Metode yang dipilih : ")

print("======================================")
print("Data Sebelum Di urutkan : ")
print(angka)
print("Data Setelah Di urutkan : ")

if pilih==('1'):
    urutasc(angka)
else:
    urutdsc(angka)

home=input("Kembali Ke Menu Utama (Y/N) ? ")
text=print("Progam Mengurutkan Data menggunaka metode Bubble sort")
back=print("")
garis=("=====================================")
if home==("Y"):
    garis
    text
 
    angka1=int(input("Masukan Bilangan ke 1 : "))
    angka2=int(input("Masukan Bilangan ke 2 : "))
    angka3=int(input("Masukan Bilangan ke 3 : "))
    angka4=int(input("Masukan Bilangan Ke 4 : "))
    angka5=int(input("Masukan Bilangan ke 5 : "))
    angka6=int(input("Masukan Bilangan ke 6 : "))
    angka7=int(input("Masukan Bilangan ke 7 : "))
    angka8=int(input("Masukan Bilangan ke 8 : "))
    angka9=int(input("Masukan Bilangan ke 9 : "))
    angka10=int(input("Masukan Bilangan ke 10 : "))
    garis

    print("Pilih Metode")
    print("1. Sorting Ascending \n2. Sorting Descending")
    pilih=input("Metode yang di pilih : ")
    garis
    print("Data Sebelum di urutkan")
    print(angka)
    print("Data Setelah Di urutkan")
    if pilih==('1') :
        urutasc(angka)
    else:
        urutdsc(angka)
    home=input("Kembali Ke Menu Utama (Y/N) ?")
else:
    back
