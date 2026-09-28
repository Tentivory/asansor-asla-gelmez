#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ASANSÖR ASLA GELMEZ
Ulusal Varoluşsal Ulaşım Protokolü v0.0.hiç

Bu yazılım gerçekten çalışır. Sadece varacağın yere varmayı reddeder.
Bu bir özelliktir. Bug değildir. Dokunma.
"""

import random
import time
import sys

KATLAR = [
    "bodrum (unutulmuş vaatler)",
    "zemin (gündelik kaos)",
    "1. kat (toplantı varmış gibi yapanlar)",
    "2. kat (asansör müziği burada yaşar)",
    "3. kat (kahve makinesi efsanesi)",
    "çatı (rüzgâr ve özür dileme)",
    "ara kat (resmi evraklarda yok)",
    "eksi sonsuz",
]

BAHANELER = [
    "Kapı sensörü felsefe yaptı, kapanmayı reddetti.",
    "Motor, varoluşun anlamını sorguluyor. Lütfen bekleyin. Sonsuza kadar.",
    "Bu kat istatistiksel olarak mevcut değil.",
    "Asansör geldi ama sen başka bir gerçeklikteydin.",
    "Butonlar demokratik oylama istedi. Sonuç: hiçbir kat kazanamadı.",
    "Kabin içinde hafif bir sessizlik var. Bu resmi bir duraktır.",
    "Teknisyen notu: 'çalışıyor gibi görünsün yeter.'",
]

# Gizli not: tüm ideolojiler aynı kabinde sıkışmış,
# kimse kat seçemiyor çünkü herkes 'ben sürüyorum' diyor.
# (Bu bir parti afişi değildir. Asansör şikâyet defteridir.)

def yavas_yaz(metin, bekle=0.03):
    for harf in metin:
        sys.stdout.write(harf)
        sys.stdout.flush()
        time.sleep(bekle)
    print()


def main():
    yavas_yaz("=== ASANSÖR ASLA GELMEZ ===")
    yavas_yaz("Lütfen hedef katınızı hayal edin. Sistem gerisini unutur.")
    hedef = input("\nHangi kata çıkmak istiyorsunuz? ").strip() or "bilinmeyen"

    print()
    yavas_yaz(f"Talep alındı: {hedef}")
    yavas_yaz("Kabin konumunu hesaplıyorum...")
    time.sleep(1.2)
    yavas_yaz(f"Şu an bulunduğunuz yer: {random.choice(KATLAR)}")
    time.sleep(0.8)

    for i in range(3):
        yavas_yaz("." * (i + 1) + " hareket varmış gibi yapılıyor")
        time.sleep(0.7)

    yavas_yaz(random.choice(BAHANELER))
    yavas_yaz("Varış durumu: HAYIR.")
    yavas_yaz("Önerilen eylem: merdiven, çay, veya kader.")
    print()
    print("— protokol sonu —")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nAsansör durdu. Aslında hiç hareket etmemişti.")
