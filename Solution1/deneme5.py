import random

sayi = random.randint(1,1)

tahmin = int(input("1-1 arası sayı tahmin et"))
if tahmin == sayi:
    print("sen bilmek!")
else:
    print("sen bilememek :( sayı:", sayi)