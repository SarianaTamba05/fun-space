#menghitung luas segitiga sederhana
def luas_segitiga():
    alas= int(input("Masukkan alas segitiga: "))
    tinggi= int(input("Masukkan tinggi segitiga: "))
    luas = alas * tinggi / 2
    print("Luas segitiga adalah: ", luas)
luas_segitiga()

#menghitung luas Persegi Panjang sederhana
def luas_persegi_panjang():
    p=int(input("Masukkan Panjang persegi: "))
    l= int(input("Masukkan Lebar Persegi: "))
    luas = p * l
    print("Luas persegi panjang adalah: ", luas)
luas_persegi_panjang()
