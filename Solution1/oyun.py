import time
import os
import random
import keyboard

Player = {
    "can": 100,
    "guc": 100,
    "savunma": 100,
    "para": 100,
    "enerji": 1000,
}
pc = True

envanter = [pc]
if envanter == ["can yüzük"]:
    Player["can"] += Player["can"] * 0.50
if envanter == ["protein barı"]:
    Player["can"] += Player["can"] * 0.10
if envanter == ["enerji içeceği"]:
    Player["enerji"] += Player["enerji"] * 0.10
if envanter == ["pc"]:
    pc = True
    kılıç = False
    
    if kılıç == True:
        print (f"kılıcın olduğu için gücün 40 arttı! gücün: {Player['guc']}")

def normal_oyuncu_değerleri():
    Player["can"] = 100
    Player["guc"] = 100
    Player["para"] = 100
    Player["savunma"] = 100
    Player["enerji"] = 1000

def durum_goster():
    print("----- DURUM -----")
    print(f"Can: {Player['can']}")
    print(f"Güç: {Player['guc']}")
    print(f"Savunma: {Player['savunma']}")
    print(f"Para: {Player['para']}")
    print(f"Enerji:{Player['enerji']}")
    print(f"Envanter:{envanter}")
    print("-----------------")

def pizza_yeme():
    print("din don! pizza is comming :)")
    fiyat = 20

    if Player["para"] >= fiyat:
        Player["enerji"] += 250
        Player["can"] += 10
        Player["para"] -= fiyat
        print(f"canın {Player['can']} paran {Player['para']}")
    else:
        print("paran bitti :(")

def kod_yazmak():
    if pc == False:
        print ("pc yok :(")
    if pc == True:
            while True:
                print ("kod yazmaya başlıyorsun...")
                time.sleep(1)
                pc_secim = input("""ne yazacaksın?
                                 1. kolay
                                 2. orta
                                 3. zor 
                                 4. Çıkış
                                """)

                if pc_secim == "4":
                    print("Kod yazmayı bıraktın.")
                    break

                if pc_secim == "1":
                    pc_secim = input ("""tmm yazmaya başla 
                                         hedef: Hello Wolrd!
                                        """)
                    if pc_secim == """print ("Hello Wolrd!")""":
                        print ("bildin!")
                    else:
                        print ("bilemedin :(")
                elif pc_secim == "2":
                    print ("""-----------------
                            tmm orta mod seçildi!
                             hedef: evet/hayır yaz:
                             evet
                             evet yazdın
                             hayır
                             hayır yazdın   
                                """)
                    cevap = input("Kodunu yaz: ")
                    if cevap == """... = input("evet/hayır yaz:")   if ... "evet":   print ("evet yazdın")   if ... "hayır"   print ("hayır yazdın")""":
                                                print ("bildin!")
                    else:
                        print ("bilemedin :(")
                elif pc_secim == "3":
                    print ("""
                       ------------------------------------------------------------------------
                       | ZOR MOD SEÇİLDİ|                                                     |
                       | HEDEF:|                                                              |
                       | naber?|                                                              |
                       | iyi|                                                                 |
                       | bende ama niye iyi sen? diye sormadın >:( sana ceza! 10 TL ni alıyom||
                       | naber?|                                                              |
                       | iyi sen?|                                                            |
                       |bende :) iyi sen dediğin için al 10 TL :)|                            |
                       -----------------------------------------------------------------------|                    
                       """)
                
                    cevap = input("Zor görev kodunu yaz: ")
                    if cevap == """
                        para = ...  ... = input("naber"):   if ... "iyi":   print ("bende ama niye iyi sen? diye sormadın >:( sana ceza! 10 TL ni alıyom")   para -= 10   elif ... "iyi sen?": print ("bende :) iyi sen dediğin için al 10 TL :)")   para += 10
                """:
                        print("bildin!")
                    else:
                        print ("bilemedin :(")
def ejderha():
    
    ejderha_guc = random.randint(100, 150)
    ejderha_can = random.randint(150, 200)
    ejderha_savunma = random.randint(50, 100)
    ejderha_enerji = random.randint(1000, 1500 )
    print ("ejderha ile savaşa gidiyorsun... ama bu seferki güçlü olacakmış :(")
    time.sleep(3)
    print ("ejderhanın yanına geldin...")
    print ("*ejderha kükremesi*")
    if ejderha_guc  and ejderha_can and ejderha_savunma and ejderha_enerji < Player["can"] and Player["guc"] and Player["savunma"] and Player["enerji"]:
        print (f"""canın {Player['can']} gücün: {Player['guc']} savunman: {Player['savunma']} enerjin: {Player['enerji']}
                   ejderha canı: {ejderha_can} ejderha gücü {ejderha_guc} ejderha savunması {ejderha_savunma} ejderha enerji: {ejderha_enerji}
                   KAZANDIN!!!
               """)
    elif ejderha_guc  and ejderha_can and ejderha_savunma > Player["can"] and Player["guc"] and Player["savunma"]:
        print (f"""canın {Player['can']} gücün: {Player['guc']} savunman: {Player['savunma']}
                   ejderha canı: {ejderha_can} ejderha gücü {ejderha_guc} ejderha savunması {ejderha_savunma}
                   KAYBETTİN!!! :(
               """)
def calısmak():
    secim2 = input ("""napacaksin?
                    1.tarımcılık
                    2. hayvancılık
                    3. garsonluk
                    """)
    secim2 == "1" or "2" or "3"
    print ("Harika! tarımcılığa başlıyorsun o zaman nereye gideceksin?")
    secim2 = input ("""
                    1. hacıkışla
                    2. istanbul
                    3.edirne
                    """)  
    secim2 == "1" or "2" or "3"
    print ("Harikahacıkışlaya gidiyorsun...")
    time.sleep(3)
    print ("hacıkışlaya geldin... tarım yapmaya başlıyorsun...")
    time.sleep(2)
    print("ama bir dakika! ne tohumun var ne suyun var nede başka bişiyin... :(")
    time.sleep(3)
    print ("ama 1 saniye hemen umudu yitirmek yok karşıda bir dükkan var gidecek misin? belkide orda tohum vb. vardır...")
    secim3 = input("") 
    if secim3 == "evet":
        print ("tmm gittin...")
        time.sleep(2)
        secim3 = input ("""ne alaceksin?
                        1.buğday tohumu (klasik tohum, içinde 60 tane tohum var) (100)
                        2. çapa
                        3.
                        """)
        if secim3 == "hayır":
            print (">:( oyun bitti")
    
def event():
    if random.randint(1, 100) <= 30:
        olay = random.randint(1, 3)
    if  olay == 1:
        kazanc = random.randint(10, 50)
        Player["para"] += kazanc
        print(f"yerde para buldun! paran:{Player['para']}")

    elif olay == 2:
        zarar = random.randint(5, 20)
        Player["can"] -= zarar
        Player["para"] -= zarar
        if Player["para"] < 0:
            Player["para"] = 0
        print(f"karşına hırsız çıktı! paran {Player['para']} canın: {Player['can']}")

    elif olay == 3:
        heal = random.randint(5, 20)
        Player["can"] += heal
        print(f"iyileştin! canın: {Player['can']}")

def dukkan():
    print ("dükkana geldin!")
    print ("ne alcaksın?")
    secim1 = input ("""
                    1.enerji içeceği (enerjini ve canını %20 arttırır) (30)
                    2.protein barı (%10 canı arttırır) (25)
                    3. yüzük (canını %50 arttırır)(100)
                    4. pc (kod yazabilirsin) (0 TL)
                    5. kılıç (gücünü 40 arttırır) (40 TL)
                    6. kalkan(savunmanı 40 arttırır) (40 TL)
                    """)
    global pc
    if secim1 == "6":
        if Player["para"] > 40:
            envanter.append("kalkan")
            print (f"kalkanı aldın! paran: {Player['para']} savunman: {Player['savunma']}")
    if secim1 == "5":
        if Player["para"] > 40:
            envanter.append("kılıç")
            print (f"kılıcı aldın! paran: {Player['para']} gücün: {Player['guc']}")
            "kılıç" == True
    
    if secim1 == "4":
        if Player["para"] > 0:
            envanter.append("pc")
            pc = True
            print (f"pc yi aldın! paran: {Player['para']}")
            
    if secim1 == "3":
        if Player ["para"] < 100:
            print (f"paran yetmiyor :( paran: {Player['para']}")
        elif Player ["para"] >= 100:
                Player['para'] -= 100
                envanter.append("can yüzük")
                Player['can'] += Player['can'] * 0.50 
                print ("ürünü başarıyla satın aldın!")
                print(f"Canın %50 arttı! Yeni can: {Player['can']} para: {Player['para']}")
    elif secim1 == "2":
        if Player["para"] < 25:
            print (f"paran yetmiyo :( paran: {Player['para']}")
        if Player["para"] > 25:
            envanter.append("protein barı")
        print (f"canın: {Player['can']}")
    elif secim1 == "1":
        if Player["para"] < 30:
            print (f"paran bitti :( paran: {Player['para']}")
        elif Player["para"] > 30:
            envanter.append("enerji içeceği")
            print (f"enerji içeceği aldın! paran: {Player['para']}")

while True:
    secim = input(
        "1.durum göstermeceeee\n"
        "2. pizza\n"
        "3. dukkan\n"
        "4. çıkış\n"
    ).strip()

    if secim == "1":
        durum_goster()
        event()

    elif secim == "2":
        pizza_yeme()
        event()

    elif secim == "3":
        dukkan()
        event()

    elif secim == "4":
        print("bb :(")
        break
    elif secim == "5":
        kod_yazmak()
        
    elif secim == "where is ejderha ?":
        ejderha()
    elif secim == "6":
        print ("kod yazarken aklıma fikir gelmediği başka meslek yapmaya karar veriyorsun...")
        calısmak()  
    else:
        print(" doğru seç >:(")

    if Player["can"] <= 0:
        print("Hey Canın 0!")
        while True:
            yeniden_deneme = input("Yeniden Dene? ").strip().lower()
            if yeniden_deneme == "evet":
                print("yeniden başladın!")
                normal_oyuncu_değerleri()
                break
            elif yeniden_deneme == "hayır":
                print("bb :(")
                exit()
            else:
                print("Lütfen 'evet' veya 'hayır' yaz.")
    if secim == "yukarıyukarıaşağıaşağısağsolsağsolabab":
        Player["can"] += 9999
        Player["enerji"] += 9999
        Player["guc"] += 9999
        Player["para"] += 9999
        Player["savunma"] += 9999
        envanter.append("protein barı")
        envanter.append("can yüzük")
        envanter.append("enerji içeceği")
        print("KONAMİ MODE AKTİF")
        print(f"""
               CAN: {Player['can']}
               ENERJİ: {Player['enerji']}
               GÜÇ:  {Player['guc']}
               PARA: {Player['para']}
               SAVUNMA: {Player['savunma']}
               ENVANTER:{envanter}
               """)
        continue