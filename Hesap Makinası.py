def carp():
    try:
        ilk_sayi = int(input("Çarpılacak ilk sayıyı giriniz: "))
        ikinci_sayi = int(input("Çarpılacak ikinci sayıyı giriniz: "))
        print(f"{ilk_sayi} * {ikinci_sayi} = {ilk_sayi * ikinci_sayi}")
    except ValueError:
        print("Sadece rakam giriniz.")


def topla():
        try:
            ilk_sayi = int(input("İlk Sayıyı Gir Tırrek: "))
            ikinci_sayi = int(input("Toplanacak ikinci sayıyı giriniz: "))
            print(f"{ilk_sayi} + {ikinci_sayi} = {ilk_sayi + ikinci_sayi}")
        except ValueError:
            print("Sadece rakam giriniz.")


def bol():
    try:
        ilk_sayi = int(input("Bölünecek sayıyı giriniz: "))
        ikinci_sayi = int(input("Bölen sayıyı giriniz: "))
        print(f"{ilk_sayi} / {ikinci_sayi} = {ilk_sayi / ikinci_sayi}")
    except ZeroDivisionError:
        print("Sayı sıfıra bölünemez.")
    except ValueError:
        print("Sadece rakam giriniz.")


def cikart():
    try:
        ilk_sayi = int(input("Çıkarılacak ilk sayıyı giriniz: "))
        ikinci_sayi = int(input("Çıkarılacak ikinci sayıyı giriniz: "))
        print(f"{ilk_sayi} / {ikinci_sayi} = {ilk_sayi - ikinci_sayi}")
    except ValueError:
        print("Sadece rakam giriniz.")


while True:
    islem_turu = input("\nNe tarz bir işlem yapmak istersiniz?"
                       "\n(Ör: + - * /)"
                       "\n(Çıkmak için 'q' yazınız.)"
                       "\nYapmak istediğiniz işlemin simgesini girin: ")

    if islem_turu == "q":
        print("Programdan çıkılıyor...")
        quit()
    elif islem_turu == '*':
        carp()
    elif islem_turu == "/":
        bol()
    elif islem_turu == "+":
        topla()
    elif islem_turu == "-":
        cikart()
    else:
        print("Geçersiz simge, tekrar deneyin.")
