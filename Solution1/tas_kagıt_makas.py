import random

print("taş kağıt makas'a hoş geldin")
print("(Oyundan çıkmak için 'çıkış' yazabilirsin)")

impossible = False
skor = 0
pc_skor = 0

while True:
    secim = input("\ntaş/kağıt/makas? ").lower().strip()

    # TÜRKÇE KARAKTER NORMALİZASYON
    secim = secim.replace("ş", "s").replace("ğ", "g").replace("ı", "i")

    if secim in ["çıkış", "cikis"]:
        print("Oyun kapatılıyor... Görüşürüz!")
        break

    elif secim == "skor":
        print(f"SEN: {skor} | PC: {pc_skor}")
        continue

    # IMPOSSIBLE MOD
    elif secim == "9647":
        impossible = True
        print("\n--- IMPOSSIBLE MOD AÇILDI ---")
        continue

    elif secim == "noimpossible":
        impossible = False
        print("\n--- IMPOSSIBLE MOD KAPANDI ---")
        continue

    # PC SEÇİMİ
    if impossible:
        pc_secim = {
            "tas": "kagit",
            "kagit": "makas",
            "makas": "tas"
        }.get(secim, random.choice(["tas", "kagit", "makas"]))
    else:
        pc_secim = random.choice(["tas", "kagit", "makas"])

    print(f"PC seçimi: {pc_secim}")  # 🔥 ARTIK HER ZAMAN GÖRÜNÜR

    # OYUN
    if secim == "tas":
        print("taş seçtin...")
        if pc_secim == "makas":
            print("KAZANDIN!")
            skor += 1
        elif pc_secim == "kagit":
            print("KAYBETTİN :(")
            pc_skor += 1
        else:
            print("BERABERE!")

    elif secim == "kagit":
        print("kağıt seçtin...")
        if pc_secim == "tas":
            print("KAZANDIN!")
            skor += 1
        elif pc_secim == "makas":
            print("KAYBETTİN :(")
            pc_skor += 1
        else:
            print("BERABERE!")

    elif secim == "makas":
        print("makas seçtin...")
        if pc_secim == "kagit":
            print("KAZANDIN!")
            skor += 1
        elif pc_secim == "tas":
            print("KAYBETTİN :(")
            pc_skor += 1
        else:
            print("BERABERE!")

    else:
        print("Sadece taş, kağıt, makas yazabilirsin.")