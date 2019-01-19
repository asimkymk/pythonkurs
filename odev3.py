"""
Problem 3
Kullanıcıdan 2 tane sayı alarak bu sayıların en küçük ortak katlarını (EKOK) dönen bir tane fonksiyon yazın.

Problem için şu siteye bakabilirsiniz;

http://www.matematikciler.com/6-sinif/matematik-konu-anlatimlari/1020-en-kucuk-ortak-kat-ve-en-buyuk-ortak-bolen-ebob-ekok
"""
print("""
EKOK BULMA PROGRMAINA HOŞ GELDİNİZ
Çıkmak için q tuşuna basınız""")

def ekok(a,b):
        for i in range(1,(a*b+1)):
            if i % b == 0 and i % a == 0:
                return i

while True:
    sayi1 = input("Sayı 1 i girin (veya çıkış) :")
    if sayi1 == "q":
        print("Çıkış yapılıyor...")
        break
    sayi2 = input("Sayı 2 i girin (veya çıkış) :")
    if sayi2 == "q":
        print("Çıkış yapılıyor...")
        break
    sayi1 = int(sayi1)
    sayi2 = int(sayi2)
    print("{} ile {} sayısının EKOK'u = {}".format(sayi1,sayi2,ekok(sayi1,sayi2)))
