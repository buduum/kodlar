import random

para = 30
anahtar = True
gizemli_anahtar = False
guc = 100
can = 100 
envanter = ["anahtar"] 
saldirma_orani = 60 # Varsayılan %60 saldırı şansı
savunma = 100
gizemli_iksir = False
kızgın_adam = False

print ("kapı dahada aşağı iniyordu aşağı indin ve başka bir mağradasın yada az öncekinin devamı? ilerledin karşında bir dükkan var ve karanlık bir tünel var hangisine gideceksin?")

while True:
    secim = input("\nNereye gideceksin? (dükkan / tünel): ").lower()

    # --- KONAMI KODU HİLESİ ---
    if secim == "yukarıyukarıaşağıaşağısağsolsağsolabab":
        print("\n!!! KONAMI KODU AKTİF EDİLDİ !!!")
        para = 10000
        guc = 10000
        can = 10000
        savunma = 10000
        gizemli_iksir = True
        gizemli_anahtar = True
        envanter.append("gizemli iksir")
        envanter.append("gizemli anahtar")
        print(f"Para: {para}, Güç: {guc}, Can: {can}, Savunma: {savunma} yapıldı! gizemli anahtar ve gizemli iksir envantere eklendi!")
        yeni_oran = input(f"Saldırı ihtimali şu an %{saldirma_orani}. Yeni oran (0-100): ")
        if yeni_oran.isdigit():
            saldirma_orani = int(yeni_oran)
            print(f"Saldırı ihtimali %{saldirma_orani} olarak güncellendi.")
        continue

    if secim == "dükkan":
        while True:
            print (f"\ndükkan a geldin {para} Paran var ne almak istersin? fiyatları görmek için fiyat yaz geri dönmek için geri dön yaz")
            secim3 = input().lower() 
            if secim3 == "fiyat":
                print ("can iksiri 20 para (canını tamanmen doldurur) güç iksiri 15 para (gücünü %40 arttırır) gizemli anahtar (???) anahtarı sat (+30 para)")
            elif secim3 == "can iksiri":
                if para >= 20:
                    para -= 20
                    can = 1000 
                    envanter.append("can iksiri")
                    print ("can iksiri aldın paran kaldı:", para)
                else:
                    print ("Yeterli paran yok!")
            elif secim3 == "güç iksiri":
                if para >= 15:
                    para -= 15
                    guc += 40
                    envanter.append("güç iksiri")
                    print ("güç iksiri aldın yeni gücün:", guc, "paran kaldı:", para)
                else:
                    print ("Yeterli paran yok!")
            elif secim3 == "gizemli anahtar":
                if para >= 30:
                    para -= 30
                    gizemli_anahtar = True
                    envanter.append("gizemli anahtar")
                    print ("gizemli anahtar aldın paran kaldı:", para)
                else:
                    print ("Yeterli paran yok!")
            elif secim3 == "anahtarı sat":
                if "anahtar" in envanter:
                    para += 30
                    anahtar = False
                    envanter.remove("anahtar")
                    print ("anahtarı sattın paran:", para)
                else:
                    print ("envanterinde anahtar yok!")
            elif secim3 == "geri dön":
                print ("dükkandan çıktın.")
                break 

    elif secim == "tünel":
        while True:
            print (f"\ntünele girdin. Paran: {para} Gücün: {guc}")
            print ("karşına bir kapı çıktı kapıyı açmak için anahtarın var mı? (yada coin ara yazabilirsin)")
            secim_tunel = input().lower()

            if secim_tunel == "coin ara":
                para += 10
                print(f"Karanlıkta 10 para buldun! Yeni paran: {para}")
                continue

            if secim_tunel == "evet":
                if anahtar:
                    print ("\nanahtarın var kapıyı açtın veeeee.........")
                    print (f"Karşında bir canavar var! (Saldırma İhtimali: %{saldirma_orani})")
                    secim5 = input("Savaş mı Konuşma mı? ").lower()
                    
                    if secim5 == "savaş":
                        canavar_guc = random.randint(50, 150)
                        print (f"canavarın gücü {canavar_guc} senin gücün {guc}")
                        if guc > canavar_guc:
                            print ("canavarı yendin ve 50 para kazandın!")
                            para += 50
                        else:
                            print ("canavar seni yendi :( oyun bitti.")
                            exit()
                    elif secim5 == "konuş" or secim5 == "konus":
                        sans = random.randint(1, 100)
                        if sans <= saldirma_orani:
                            print ("Canavar konuşmana izin vermedi ve saldırdı!")
                            canavar_guc = random.randint(80, 160)
                            if guc > canavar_guc:
                                print ("Hazırlıksız yakalansan da kazandın!")
                            else:
                                print ("Canavar seni yok etti...")
                                exit()
                        else:
                            print ("Arkadaş oldunuz! Canavar sana 20 para verdi.")
                            para += 20
                else:
                    print ("anahtarın yok! Kapıyı açamadın.")
                    break

                print ("tünelden çıktın.")
                print ("ve karşına bir kapı çıktı kapıyı açmak için anahtarın var mı? (yada coin ara yazabilirsin)")
                secim_son = input("evet/hayır: ").lower()
                
                if secim_son == "evet":
                    if anahtar:
                        print ("anahtarın var kapıyı açtın veeeee.........")
                        print ("karşında 2  yol var (gizemli bina / dümdüz) hangisine gideceksin?")
                        secim2 = input("gizemli bina mı dümdüz mü?").lower()
                        if secim2 == "gizemli bina":
                            print ("gizemli binaya girdin veyaşlı bir bilge sana buranın tarihini anlattı dinleyecek misin?")
                            secim3 = input("evet/hayır: ").lower()
                            if secim3 == "evet":
                                print ("bilge sana bu mağranın çooooook eskilere dayandığını ve eskiden burda bir sürü insanın yaşadağını ve ayrıca hala burda onların gizli hazineleri olduğuna inanılıyor")
                                secim4 = input("hazineleri araştırmak ister misin? evet/hayır: ").lower()
                                if secim4 == "evet":
                                    print ("hazineleri araştırmaya başladın ve gizemli bir sandık buldun sandığı açmak ister misin? evet/hayır: ")
                                    secim5 = input().lower()
                                    if secim5 == "evet":
                                        print ("sandığı açtın ve içinden 100 para çıktı!")
                                        para += 100
                                    else:
                                        print ("sandığı açmadın ve mağaradan çıktın.")
                                else:
                                    print ("yoluna devam ediyorsun")
                                
                                print ("dümdüz devam ettin ve karşına bir kapı çıktı kapıyı açmak için anahtarın var mı? (yada coin ara yazabilirsin)")
                                secim_kapı2 = input("evet/hayır: ").lower()
                                if secim_kapı2 == "evet":
                                    if gizemli_anahtar:
                                        print ("anahtarın var kapıyı açtın veeeee.........")
                                        print ("yoluna devam ettin")   
                                        print ("kod yazmayı seviyorum ama aklıma fikir gelmiyo çok neyse dur bi market fln olsun eşylaral kılıç fln ee tmm buldum")
                                        print ("karşına bir dükkan çıktı dükkana girmek ister misin? evet/hayır: ")
                                        secim_market_giris = input("evet/hayır: ").lower()
                                        if secim_market_giris == "evet":
                                            # --- DÜZELTİLEN İKİNCİ MARKET DÖNGÜSÜ ---
                                            while True:
                                                print (f"\nDükkandasın. Paran: {para}. Fiyatlara bakmak ister misin? evet/hayır (veya geri dön)")
                                                secim_fiyat = input().lower()
                                                if secim_fiyat == "evet":
                                                    print ("kristal kılıç 40 para (gücünü %50 arttırır) can iksiri 20 para (canına ekstradan 20 can ekler) kalkan 30 para (savunmanı %30 arttırır) gizemli iksir 999 para (???)")
                                                    print ("ne almak istersin? geri dönmek için geri dön yaz")
                                                    secim_al = input().lower()
                                                    if secim_al == "kristal kılıç":
                                                        if para >= 40:
                                                            para -= 40
                                                            guc += 50
                                                            envanter.append("kristal kılıç")
                                                            print ("kristal kılıç aldın yeni gücün:", guc, "paran kaldı:", para)
                                                        else: print ("Yeterli paran yok!")
                                                    elif secim_al == "can iksiri":
                                                        if para >= 20:
                                                            para -= 20
                                                            can = 120 
                                                            envanter.append("can iksiri")
                                                            print ("can iksiri aldın paran kaldı:", para)
                                                        else: print ("Yeterli paran yok!")
                                                    elif secim_al == "kalkan":
                                                        if para >= 30:
                                                            para -= 30
                                                            envanter.append("kalkan")
                                                            print ("kalkan aldın paran kaldı:", para)
                                                        else: print ("Yeterli paran yok!")
                                                    elif secim_al == "gizemli iksir":
                                                        if para >= 999:
                                                            para -= 999
                                                            envanter.append("gizemli iksir")
                                                            print ("gizemli iksir aldın paran kaldı:", para)
                                                        else: print ("Yeterli paran yok!")
                                                    elif secim_al == "geri dön":
                                                        break
                                                elif secim_fiyat == "hayır" or secim_fiyat == "geri dön":
                                                    break

                                            # --- MARKET ÇIKIŞI HİKAYE ---
                                            print ("yoluna devam ediyorsun")
                                            print ("dümdüz devam ettin ve karşına bir adam çıktı adam senden biraz para istedi para vercek misin? evet/hayır: ")
                                            secim_adam = input("evet/hayır: ").lower()
                                            if secim_adam == "evet":
                                                print ("adama ne kadar para vereceksin?")
                                                print ("1. 10 coin 2. 20 coin 3. 50 coin")
                                                secim_miktar = input("1/2/3: ").lower()
                                                if secim_miktar == "1" and para >= 10:
                                                    para -= 10
                                                    para += 20
                                                    print ("adama 10 coin verdin, o sana 20 coin verdi! paran:", para)
                                                elif secim_miktar == "2" and para >= 20:
                                                    para -= 20
                                                    para += 30
                                                    print ("adama 20 coin verdin, o sana 30 coin verdi! paran:", para)
                                                elif secim_miktar == "3" and para >= 50:
                                                    para -= 50
                                                    para += 60
                                                    print ("adama 50 coin verdin, o sana 60 coin verdi! paran:", para)
                                            else:
                                                print ("adama para vermedin yoluna devam ediyorsun")
                                                print ("adam bunun intikamını senden alacağını söyledi ")
                                                kızgın_adam = True
                                            
                                            print ("yoluna devam ediyorsun")
                                            print ("fikirim kalmadı eğer'tmm' yazarsan oyun bitcek 'devam' yazarsan devam edecek")
                                            secim_bitis = input("tmm/devam: ").lower()
                                            if secim_bitis == "tmm":
                                                print ("oyunu bitirdin tebrikler!")
                                                exit()
                                            elif secim_bitis == "devam":
                                                print ("yoluna devam ediyorsun")
                                                print ("zaten 240 satır kod yazdım buda 241 kod satırı oldu fikrim kalmadı artıkhadi oyun bitti yapan kişilerin şeyide akcak birazdan hadi böle creditler oluyo ya filmlerin yada oyunların sonunda ya nese hadi oyun bitti tebrikler 3. yü çıkatırmıyım bilmiyorum hadi bitti oyun")
                                                print ("oyunu bitirdin tebrikler!")
                                                print ("yapımcılar: ömer, ömer, ömer, ömer, ömer, ömer, ömer, ömer, ömer, ömer")
                                                print ("fikir: ömer")
                                                print ("kodlama: ömer")
                                                print ("test: ömer (üşendiği için daha test etmedi) ")
                                                print ("tasarım: ömer")
                                                print ("herşey: ömer")
                                                print ("tekrar oynarsan belki yeni şeyler eklerim ")
                                                print ("son yazdığım kapatma kodu ile toplam 251 satır kod oldu hadi bb")
envanter_metni = ",".join(envanter) 

with open("kayit_dosyasi.txt", "w") as dosya:
    dosya.write(f"{para}\n")
    dosya.write(f"{guc}\n")
    dosya.write(f"{can}\n")
    dosya.write(f"{savunma}\n")
    dosya.write(f"{str(kızgın_adam)}\n")
    dosya.write(f"{envanter_metni}\n")

print("Sistem: Tüm veriler (Envanter dahil) başarıyla kaydedildi!")
exit()