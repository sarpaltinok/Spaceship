import pygame
import random

# Ekran boyutları
EKRAN_GENISLIK = 800
EKRAN_YUKSEKLIK = 600

# Renkler
BEYAZ = (255, 255, 255)
SIYAH = (0, 0, 0)

class UzayGemisi(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 30))
        self.image.fill((255, 0, 0))  # Kırmızı bir dikdörtgen şeklinde gemi
        self.rect = self.image.get_rect()
        self.rect.center = (100, EKRAN_YUKSEKLIK // 2)
        self.hiz = 0

    def update(self):
        self.hiz = 0
        tuslar = pygame.key.get_pressed()
        if tuslar[pygame.K_UP]:
            self.hiz = -5
        if tuslar[pygame.K_DOWN]:
            self.hiz = 5
        self.rect.y += self.hiz
        # Ekran sınırlarını kontrol etmek için
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= EKRAN_YUKSEKLIK:
            self.rect.bottom = EKRAN_YUKSEKLIK

class Engeller(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, random.randint(100, 300)))
        self.image.fill((0, 255, 0))  # Yeşil bir dikdörtgen şeklinde engeller
        self.rect = self.image.get_rect()
        self.rect.left = EKRAN_GENISLIK
        self.rect.bottom = random.randint(50, EKRAN_YUKSEKLIK - 50)
        self.hiz = 5

    def update(self):
        self.rect.x -= self.hiz
        if self.rect.right < 0:
            self.rect.left = EKRAN_GENISLIK
            self.rect.bottom = random.randint(50, EKRAN_YUKSEKLIK - 50)

def main():
    pygame.init()
    ekran = pygame.display.set_mode((EKRAN_GENISLIK, EKRAN_YUKSEKLIK))
    pygame.display.set_caption("Uzay Gemisi Kaçışı")
    sahne = pygame.Surface(ekran.get_size())
    saat = pygame.time.Clock()

    oyuncu = UzayGemisi()
    oyuncu_group = pygame.sprite.Group()  # Oyuncu için sprite grubu
    oyuncu_group.add(oyuncu)

    engel_listesi = pygame.sprite.Group()
    for i in range(6):
        engel = Engeller()
        engel_listesi.add(engel)

    calisma = True
    while calisma:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                calisma = False

        oyuncu.update()
        engel_listesi.update()

        # Çarpışma kontrolü
        if pygame.sprite.spritecollide(oyuncu, engel_listesi, False):
            print("Oyun bitti!")
            calisma = False

        sahne.fill(SIYAH)
        oyuncu_group.draw(sahne)  # Oyuncu grubunu sahneye çiz
        engel_listesi.draw(sahne)
        ekran.blit(sahne, (0, 0))
        pygame.display.flip()
        saat.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
