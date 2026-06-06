import pygame
import math

# 1. BAŞLATMA
pygame.init()
ekran = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
genislik, yukseklik = ekran.get_size()
pygame.display.set_caption("SİOİH")

# Dosyalar kodunla aynı klasörde olmalı
try:
    karakter_resmi = pygame.image.load("SİOİH karakter.png").convert_alpha()
    lamba_kapali = pygame.image.load("lamba_kapalı.png").convert_alpha() # 'ı' harfine dikkat edildi
    lamba_acik = pygame.image.load("lamba_acık.png").convert_alpha()
except pygame.error as e:
    print(f"Resim yükleme hatası! Dosya isimlerini kontrol et: {e}")
    # Eğer dosyalar bulunamazsa oyun çökmesin diye boş yüzeyler oluşturur
    karakter_resmi = pygame.Surface((50, 50)); karakter_resmi.fill((255, 0, 0))
    lamba_kapali = pygame.Surface((60, 60)); lamba_kapali.fill((50, 50, 50))
    lamba_acik = pygame.Surface((60, 60)); lamba_acik.fill((255, 255, 0))

# 3. DEĞİŞKENLER
x, y = 200, 200
hiz = 8
l_x, l_y = genislik // 2, yukseklik // 2 
lamba_durumu = False # Başlangıçta ışık kapalı

saat = pygame.time.Clock()
calisiyor = True

# 4. OYUN DÖNGÜSÜ
while calisiyor:
    # Olay Kontrolü
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            calisiyor = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                calisiyor = False
            
            # F tuşuna basıldığında ve karakter lambaya yakınsa
            mesafe = math.hypot(x - l_x, y - l_y)
            if event.key == pygame.K_f and mesafe < 120:
                lamba_durumu = not lamba_durumu

    # Hareket Sistemi
    tuslar = pygame.key.get_pressed()
    if tuslar[pygame.K_LEFT] and x > 0: x -= hiz
    if tuslar[pygame.K_RIGHT] and x < genislik - 50: x += hiz
    if tuslar[pygame.K_UP] and y > 0: y -= hiz
    if tuslar[pygame.K_DOWN] and y < yukseklik - 50: y += hiz


    # Nesneleri ekrana bas
    ekran.blit(lamba_kapali.png, (l_x, l_y))
    ekran.blit(karakter_resmi.png, (x, y))

    pygame.display.flip()
    saat.tick(60)

pygame.quit()
