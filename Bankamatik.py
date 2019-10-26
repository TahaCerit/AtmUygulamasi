print("********************\nBeta ATM Uygulamasına Hoşgeldiniz\n********************")

print("""
İşlemler:

1. Bakiye Sorgulama
2. Para Yatırma
3. Para Çekme

Programdan 'q' tuşu ile çıkabilirsiniz.

""")

bakiye  = 500
while True:
    işlem = input("İşleminizi Giriniz:")
    if (işlem == "q"):
        print("Yine Bekleriz...")
        break
    elif (işlem == "1"):
        print("Bakiyeniz {} tl dir.".format(bakiye))
    elif (işlem == "2"):
        miktar = int(input("Yatırmak İstediğiniz Tutarı Giriniz:"))
        bakiye += miktar
        print ("İşleminiz Yatırılıyor...")
    elif (işlem == "3"):
        miktar = int(input("Çekmek İstediğiniz Tutarı Giriniz:"))
        if(bakiye - miktar < 0):
            print("Yetersiz Bakiye...")
            print("Bakiyeniz {} tl dir.".format(bakiye))
            continue
        bakiye-=miktar

        print("Paranız Çekiliyor...")
    else:
        print("Lütfen Geçerli Bir İşlem Giriniz...")




