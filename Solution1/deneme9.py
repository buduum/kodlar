import time
import os
import random

# --- GERİ SAYIM FONKSİYONU
def geri_say(saniye):
    for i in range(saniye, 0, -1):
        print(f"[{i} saniye kaldı...]", end="\r", flush=True)
        time.sleep(1)
    print(" İşlem tamamlandı!          ")

# --- KAYIT YÜKLEME
if os.path.exists("kayit_dosyasi.txt"):
    with open("kayit_dosyasi.txt", "r") as dosya:
        satirlar = dosya.readlines()

    match len(satirlar):
        case n if n >= 6:
            try:
                para = int(satirlar[0].strip())
                guc = int(satirlar[1].strip())
                can = int(satirlar[2].strip())
                savunma = int(satirlar[3].strip())
                kızgın_adam = satirlar[4].strip() == "True"

                envanter_ham = satirlar[5].strip()
                envanter = envanter_ham.split(",") if envanter_ham else []

                print(f"\n--- KAYIT YÜKLENDİ ---")
                print(f"Para: {para}, Güç: {guc}, Can: {can}, Savunma: {savunma}")
                print(f"Envanter: {envanter}")

            except ValueError:
                print("Kayıt dosyasındaki veriler bozuk! Yeni oyun başlatılıyor...")
                para, guc, can, savunma = 30, 100, 100, 100
                envanter, kızgın_adam = [], False

        case _:
            print("Kayıt dosyası eksik veya boş! Maceracı baştan yaratılıyor...")
            para, guc, can, savunma = 30, 100, 100, 100
            envanter, kızgın_adam = [], False

else:
    print("Kayıt bulunamadı, yeni macera başlıyor!")
    para, guc, can, savunma = 30, 100, 100, 100
    envanter, kızgın_adam = [], False


az_kızgın_adam = False
cok_kızgın_adam = False
kahveyapanayrıcakahvedağıtanvemasalarısilenrobot_3000 = False
pc = False
kılıc = False

secim = {
    "sihirbaz": "",
    "is": "",
    "kafe": "",
    "gorev": "",
    "kavga": "",
    "uyku": "",
    "mesai": "",
    "dükkan": "",
    "konami": "",
    "ev_secimi": "",
    "dükkana_geri_dönme": "",
    "cıkıs": ""
}

# --- KONAMI KODU (if yoktu, match zaten doğru)
match secim["konami"]:
    case "yukarıaşağısağsolabab" | "yukarıyukarıaşağıaşağısağsolsağsolabab":
        para += 9999
        guc += 9999
        savunma += 9999
        can += 9999
        print(f"paran: {para} gücün: {guc} savunman: {savunma} can: {can}")

print("yoluna devam ediyorsun... karşına bir sihirbaz çıktı izlicek misin?")

while True:
    secim["sihirbaz"] = input("evet/hayır? ").strip().lower()

    match secim["sihirbaz"]:
        case "evet":
            para = 0
            print(f"izliyorsun... adam cebindeki parayı uçurarak paranı aldı ve görünmez olup kaçtı {para} paran kaldı")
            break

        case "hayır":
            print("adam kafanı sihir ile çevirerek zorla izletti")
            para = 0
            print(f"izliyorsun... adam cebindeki parayı uçurarak paranı aldı ve görünmez olup kaçtı {para} paran kaldı")
            break

        case _:
            print("Geçersiz girdi! Lütfen sadece 'evet' veya 'hayır' yazın.")

time.sleep(1)
print("para kazanman lazım... fikir arıyorsun")
time.sleep(1)

while True:
    secim["is"] = input("""
napacaksın?
1. garsonluk
2. garsonluk
3. garsonluk
4. garsonluk
Seçiminiz: """).strip()

    match secim["is"]:
        case "1" | "2" | "3" | "4":
            print("tmm garsonculuğa başlıyorsun")
            print("nereye gideceksin?")
            break

        case _:
            print("Geçersiz seçim! Lütfen listedeki sayılardan birini girin.")

while True:
    secim["kafe"] = input("""
1. kafi kafe
2. kafi kafe
3. kafi kafe

Seçiminiz: """).strip()

    match secim["kafe"]:
        case "1" | "2" | "3":
            print("kafi kafeye gidiyorsun... patronun sana iş veriyor")
            time.sleep(1)
            break

        case _:
            print("Geçersiz kafe seçimi! Lütfen 1, 2 veya 3 yazın.")

while True:
    secim["gorev"] = input("""
1. masaları temizle
2. masaları temizle
3. masaları temizle

Seçiminiz: """).strip()

    match secim["gorev"]:
        case "1" | "2" | "3":
            print("masaları temizliyorsun... patronun sana para veriyor")
            print("not: masaları silmek zaman aldığı için sayaç başlıyor:")
            geri_say(30)
            para += 10
            print(f"para kazanman random... şu anki paran {para}")
            time.sleep(1)
            break

        case _:
            print("Geçersiz görev! Patron düzgün bir şey seçmeni bekliyor.")

print("işten çıkıyorsun... patronun sana iyi günler diliyor")

# --- KIZGIN ADAM
match kızgın_adam:
    case True:
        print("Karşına Tanıdık Bir Yüz Çıkıyor... Kızgın Adam!")

        while True:
            secim["kavga"] = input("""
1. kaç
2. Saldır

Seçiminiz: """).strip()

            match secim["kavga"]:
                case "1":
                    sayi = random.randint(1, 5)

                    match sayi <= 3:
                        case True:
                            print("kaçıyorsun... adam seni yakalıyor ve dövüyor")
                            can -= 20
                            print(f"canın azaldı... şu anki canın {can}")
                            az_kızgın_adam = True
                            cok_kızgın_adam = False

                        case False:
                            print("kaçıyorsun... adam seni yakalayamadı ve kaçmayı başarıyorsun")
                            az_kızgın_adam = False
                            cok_kızgın_adam = True

                    break

                case "2":
                    sayi = random.randint(1, 5)

                    match sayi <= 3:
                        case True:
                            print("saldırıyorsun... adam seni yakalıyor ve dövüyor")
                            can -= 20
                            time.sleep(1)
                            print(f"canın azaldı... şu anki canın {can}")
                            cok_kızgın_adam = False
                            az_kızgın_adam = True

                        case False:
                            print("saldırıyorsun... adam seni yakalayamadı ve saldırını savuşturuyorsun")
                            cok_kızgın_adam = True
                            az_kızgın_adam = False
                            time.sleep(1)

                    break

                case _:
                    print("Geçersiz seçim. Düzgün bir hamle seç!")

    case _:
        pass

print("evine geldin çok yorgunsun...")

while True:
    secim["uyku"] = input("""
1. uyu
2. uyu

Seçiminiz: """).strip()

    match secim["uyku"]:
        case "1" | "2":
            print("uyuyorsun... canın yenileniyor:")
            geri_say(10)
            can = 100
            print(f"canın yenilendi... şu anki canın {can}")
            break

        case _:
            print("Geçersiz seçim! Yorgunluktan bayılmadan önce düzgün bir seçim yap.")

print("aağğghh *esneme* yeni bir day yeni bir iş kafi kafeye gidiyorsun...")
print("kafi kafeye geldin... patronun bugün daha az mesai yapabilceğini söylüyor")

while True:
    secim["mesai"] = input("""
1. az mesai
2. normal mesai
3. çok mesai

Seçiminiz: """).strip()

    match secim["mesai"]:
        case "1":
            print("tmm biraz kestiriyorsun:")
            geri_say(10)
            print("işin bittiği için eve dönüyorsun")
            para += 10
            break

        case "2":
            print("Bugün normal mesai çalışıyorsun.")
            print("masaları siliyorsun:")
            geri_say(5)
            print("işin bittiği için eve dönüyorsun")
            para += 30
            break

        case "3":
            print("Çok mesai yapıyorsun.")
            print("patronun seni tebrik etti o yüzden az çalışmana izin verdi :) ")
            para += 40
            print("işin bittiği için eve dönüyorsun")
            break

        case _:
            print("Geçersiz seçim! Patronun yüzüne boş boş bakıyorsun...")

print("eve dönerken karşına bir dükkan çıkıyor. bişi alcak mısın? (evet/hayır)")

while True:
    secim["dükkan"] = input("").strip().lower()

    match secim["dükkan"]:
        case "evet":
            print("""fiyatlar:
1. kahveyapanayrıcakahvedağıtanvemasalarısilenrobot 3000: 999 TL
2. kılıç: 80 tl (gücünü 40 arttırır)
3. pc: 100 TL (kod yazabilirsin) (AŞIRII TAVSİYE EDİLİYORMUŞ)
""")

            satın_alınan = input("Almak istediğiniz ürünün adını aynen yazın: ").strip()

            match satın_alınan:
                case "kahveyapanayrıcakahvedağıtanvemasalarısilenrobot 3000":
                    match para >= 999:
                        case True:
                            para -= 999
                            kahveyapanayrıcakahvedağıtanvemasalarısilenrobot_3000 = True
                            print(f"kahveyapanayrıcakahvedağıtanvemasalarısilenrobot 3000 aldın! paran: {para}")

                        case False:
                            print(f"paran yetmiyo :( paran {para}")

                case "kılıç":
                    match para >= 80:
                        case True:
                            guc += 40
                            para -= 80
                            print(f"kılıcı almak sen! sen para kalmak: {para}")

                        case False:
                            print(f"paran yetmiyo :/ paran {para}")

                case "pc":
                    match para >= 100:
                        case True:
                            para -= 100
                            pc = True
                            print(f"sen almak pc sen para kalmak {para}")

                        case False:
                            print(f"sen alamamak pc sen para yetmemek sen para {para}")

                case _:
                    print("Dükkanda böyle bir ürün bulunamadı.")

            break

        case "hayır":
            print("Dükkana uğramadan yoluna devam ediyorsun.")
            break

        case _:
            print("Lütfen sadece 'evet' veya 'hayır' yazın.")
time.sleep(2)
print("yoluna devam ediyorsun")
time.sleep(1)
print("yoluna devam ediyorsun.")
time.sleep(1)
print("yoluna devam ediyorsun..")
time.sleep(1)
print("yoluna devam ediyorsun...")
time.sleep(3)

print("eve geldin napacaksın?")

match pc:
    case False:
        secim["ev_secimi"] = input("""
1. uyu
2. HAYATI SORGULA

Seçiminiz: """).strip().lower()

        match secim["ev_secimi"]:
            case "1":
                print("uyuyorsun")
                geri_say(10)
                print("aklına pc yi almak geliyor o yüzden sıkı çalışman lazım yadaa... bu benden sana bir hediye olsun +100 TL yada neyse ben kendim alıp sana vercem o 100 TL yi geri alıyom")

                match secim.get("dükkana_geri_dönme", ""):
                    case "geri dön":
                        print("geri döndün napacan? şaka şaka biliyom pc alcan al sana pc:")
                        pc = True
                    case _:
                        pass

            case "2":
                print("hayatı sorguluyorsun...")
                geri_say(10)
                print("hayatı sorguladın... iyi geldi")

            case _:
                print("Geçersiz seçim!")

    case True:
        pass


match secim["cıkıs"]:
    case "cıkıs":
        print("çıkıyorsun... bb :(")
        exit()

    case _:
        pass