import random
sayi = random.randint(1,100)
while True:
    tahmin = int(input("sen tahmin etmek 1 ile 100 arası sayı "))

    if tahmin > sayi:
        print("daha küçük")
    elif tahmin < sayi:
        print("daha büyük")
    else:
        print("sen bilmek")
        break