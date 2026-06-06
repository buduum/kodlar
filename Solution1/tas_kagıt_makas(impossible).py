import random

print("taş kağıt makas'a hoş geldin")
print("(Oyundan çıkmak için 'çıkış' yazabilirsin)")

konami_code = False
skor = 0
pc_skor = 0
ekstra_puan_miktari = 1

while True:
    secimler = ["tas", "kagit", "makas",]
    pc_secim = {
        "tas": "kagıt"
        "kagit": "makas"
        "makas": "tas"
    }.get(secim, "tas")
    secim = input("\ntaş/kağıt/makas? ").lower().strip()

    if secim == "çıkış" or secim == "cikis":
        print("Oyun kapatılıyor... Görüşürüz!")
        break

    elif secim == "skor":
        print(f"SEN: {skor} | PC: {pc_skor}")
        continue

    # KONAMİ KODU
    elif secim in [
        "yukarıyukarıaşağıaşağısağsolsağsolabab",
        "yukarıaşağısağsolabab",
        "yukariyukariasagiasagisagsolsagsolabab"
    ]:
        konami_code = True
        print("\n--- KONAMİ MODU AKTİF EDİLDİ! ---")
        try:
            ekstra_puan_miktari = int(input("Her kazandığınızda kaç puan gelsin?: "))
        except ValueError:
            ekstra_puan_miktari = 10
        continue

    elif secim == "nokonami":
        konami_code = False
        ekstra_puan_miktari = 1
        continue

    # OYUN MEKANİĞİ
    elif secim == "tas" or secim == "taş":
        print("taş seçtin...")
        if pc_secim == "makas":
            print(f"pc {pc_secim} seçti: KAZANDIN!")
            skor += ekstra_puan_miktari
        elif pc_secim == "kagit":
            print(f"pc {pc_secim} seçti: KAYBETTİN :(")
            pc_skor += 1
        else:
            print(f"pc {pc_secim} seçti: BERABERE!")

    elif secim == "kagit" or secim == "kağıt":
        print("kağıt seçtin...")
        if pc_secim == "tas":
            print(f"pc {pc_secim} seçti: KAZANDIN!")
            skor += ekstra_puan_miktari
        elif pc_secim == "makas":
            print(f"pc {pc_secim} seçti: KAYBETTİN :(")
            pc_skor += 1
        else:
            print(f"pc {pc_secim} seçti: BERABERE!")

    elif secim == "makas":
        print("makas seçtin...")
        if pc_secim == "kagit":
            print(f"pc {pc_secim} seçti: KAZANDIN!")
            skor += ekstra_puan_miktari
        elif pc_secim == "tas":
            print(f"pc {pc_secim} seçti: KAYBETTİN :(")
            pc_skor += 1
        else:
            print(f"pc {pc_secim} seçti: BERABERE!")

    else:
        print("Sadece taş, kağıt, makas veya çıkış yazabilirsin.")