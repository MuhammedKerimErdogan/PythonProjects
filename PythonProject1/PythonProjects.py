print("Lutfen yapmak istediginiz islemi seciniz:\n1-)Toplama\n2-)Cikarma\n3-)Carpma\n4-)Bolme\n5-)Mod Alma\n6-)Us Alma")
secim = input("Yapmak istediginiz islemi seciniz : ")
sayi1 = int(input("Lutfen ilk sayiyi giriniz : ")) 
sayi2 = int(input("Lutfen ikinci sayiyi giriniz : "))
if secim == "1":
    sonuc = sayi1 + sayi2
    print("Toplam :", sonuc)
elif secim == "2":
    sonuc = sayi1 - sayi2
    print("Fark :", sonuc)
elif secim == "3":
    sonuc = sayi1 * sayi2
    print("Carpim :", sonuc)
elif secim == "4":
    sonuc = sayi1 / sayi2
    print("Bolum :", sonuc)
elif secim == "5":
    sonuc = sayi1 % sayi2
    print("Sonuc :", sonuc)
elif secim == "6":
    sonuc = sayi1 ** sayi2
    print("Sonuc :", sonuc)
else:
    print("Gecersiz Islem , Lutfen Tekrar Deneyiniz !")
