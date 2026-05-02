import random
import time
import statistics

# --- ÖDEV PARAMETRELERİ ---
OGRENCI_NO = 5230505068
random.seed(OGRENCI_NO)

N = 10**6  # Veri Hacmi
K = 2500   # Sabit İterasyon Sayısı (Monte Carlo)

# 1. Veri Seti Oluşturma
print(f"1 Milyon elemanlı dizi oluşturuluyor...")
# Koşulu sağlayan elemanların oranını kontrol etmek için 1-1.000.000 arası sayılar
veri_seti = [random.randint(1, 1000000) for _ in range(N)]

def monte_carlo_arama(data, iterations):
    """Belirli bir iterasyonda koşulu sağlayan eleman arar."""
    for _ in range(iterations):
        idx = random.randint(0, len(data) - 1)
        # Koşul: Sayının 1000'e tam bölünmesi
        if data[idx] % 1000 == 0:
            return True  # Başarılı
    return False  # Hata (Bulunamadı)

# 2. Deneyin 100 Kez Çalıştırılması
deney_sayisi = 100
sonuclar = []
sureler = []

print(f"Deney başlatıldı (100 tekrar)...")
for i in range(deney_sayisi):
    baslangic = time.time()
    sonuc = monte_carlo_arama(veri_seti, K)
    bitis = time.time()
    
    sonuclar.append(sonuc)
    sureler.append(bitis - baslangic)

# 3. Analiz ve Çıktı
basari = sonuclar.count(True)
hata = sonuclar.count(False)
ortalama_sure = statistics.mean(sureler)
std_sapma = statistics.stdev(sureler)

print("\n--- ANALİZ SONUÇLARI ---")
print(f"Teorik Hata Payı: %8.2")
print(f"Deneysel Hata Sayısı: {hata} / {deney_sayisi}")
print(f"Deneysel Hata Oranı: %{(hata/deney_sayisi)*100}")
print(f"Ortalama Süre: {ortalama_sure:.6f} sn")
print(f"Süre Standart Sapması: {std_sapma:.6f} sn")