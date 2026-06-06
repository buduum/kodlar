anahtar = False 

while True: 
    print ("\nbir mağradasın önünde 2 yol var: sağ ve sol hangisine gideceksin?")
    secim = input ("Sol mu Sağ mı?").lower()

    if secim == "sol":
        print ("sola gittin... önünde bir nehir var yüzerek mi geçeceksin yoksa köprü mü arayacaksın? ")
        secim2 = input() 
        if secim2 == "yüzerek":
            print ("timsahlar seni yedi :( en baştan başlat")
            continue 
            
        if secim2 == "köprü":
            
            if anahtar == True:
                print("köprü buldun ve güvenlice karşıya geçtin. bir kapı var ama anahtarın olduğu için kapıyı açabiliyorsun 1. bölümü bitirdin!")
                break #BURASI DEĞİŞECEK: Oyunu bitirir
            else:
                print ("köprü buldun ve güvenlice karşıya geçtin. vee.... karşında bir kapı var kapıya koştun ama anahtar lazım anahtarın yoksa en baştan başlat anahtar bulup gel")
                continue

    elif secim == "sağ" or secim == "sag":
        print ("sağ gittin... karşında uyuyan bir ejderha var saldırcak mısın yoksa sesizce yanından mı geçeceksin?")
        secim2 = input()
        if secim2 == "saldır":
            print ("ejderha seni ateş püskürterek yok etti :( enbaştan başlat")
            continue 
            
        elif secim2 == "sessizce":
            print ("sesizce ilerledin ve bir anahtar buldun! şimdi geri dön yazarak geri döne bilirsin! belki bir kapı")
            anahtar = True
            #BURASI DEĞİŞECEK: Geri dönme komutu kontrolü
            geri_don = input()
            if geri_don == "geri dön":
                continue
    else:
        print ("geçersiz seçim kayboldun :(")
        continue 