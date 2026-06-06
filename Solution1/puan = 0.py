puan = 0
bilememe = 0

def soru1():
    secim = input ("Kaplan mı daha hızlı aslan mı?").lower
    if secim == "kaplan":
        print ("bildin")
        puan + 1
    elif secim == "aslan":
        print ("bilemedin :(")
        bilememe + 1
        
soru1