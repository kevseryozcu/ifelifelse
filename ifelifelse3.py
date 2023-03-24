print("""***************


işlemler:

1.toplama
2.çıkarma
3.çarpma
4.bölme


***************""")

a = int(input("birinci sayı: "))
b = int(input("ikinci sayı: "))
islem = input("işlemin giriniz: ")

if islem == "1":
    print("{} ile {} toplamı {} dir".format(a, b, a+b))
elif islem == "2":
    print("{} ile {} farkı {} dir".format(a, b, a-b))
elif islem == "3":
    print("{} ile {} çarpımı {} dir".format(a, b, a*b))
elif islem == "4":
    print("{} ile {} in bölümü {} dir".format(a, b, a/b))
else:
    print("geçerli bir işlem numarası giriniz (1-2-3-4)")

# basit bir hesap makinesi
