# Monte-Carlo-Algorithm-Analysis
# Olasılıksal Algoritmaların Deneysel Analizi

Bu proje, Kırklareli Üniversitesi Yazılım Mühendisliği Bölümü **Algoritma Analizi** dersi ödevi kapsamında hazırlanmıştır. Projede, büyük veri setleri üzerinde Monte Carlo ve Las Vegas yaklaşımının performans ve doğruluk analizi yapılması amaçlanmıştır.

## 👤 Öğrenci Bilgileri
* **Ad Soyad:** Burak Çavuşoğlu[cite: 1]
* **Öğrenci No:** 5230505068[cite: 1]
* **Üniversite:** Kırklareli Üniversitesi[cite: 1]

## 🛠️ Uygulama Parametreleri
Öğrenci numarasının son iki hanesine (68) göre belirlenen parametreler şunlardır:
* **Algoritma Tipi:** Monte Carlo Yaklaşımı (Son rakam 8/Çift olduğu için)[cite: 1]
* **Veri Hacmi (n):** 1.000.000 (Son rakam Y >= 5 olduğu için)[cite: 1]
* **İterasyon Sayısı (k):** 2500[cite: 1]
* **Seed Zorunluluğu:** 5230505068 (Rastgele sayı üreticisi öğrenci numarası ile beslenmiştir)[cite: 1]

## 📝 Problem Tanımı
Rastgele üretilmiş 1 milyon elemanlı bir dizi içerisinde, belirli bir koşulu (mod 1000'e göre 0 kalanını veren elemanlar) sağlayan verilerin tespiti hedeflenmiştir. Monte Carlo yaklaşımı kullanılarak belirli bir `k` iterasyonu sonunda hata yapma olasılığı ($P(error)$) teorik ve deneysel olarak karşılaştırılmıştır.

## 📊 Özet Bulgular
* **Teorik Hata Payı:** %8.2[cite: 1]
* **Zaman Karmaşıklığı:** O(k)[cite: 1]
* **Analiz:** Monte Carlo yaklaşımı kullanıldığı için çalışma süreleri arasındaki standart sapma oldukça düşük çıkmıştır. Bu durum, rastgeleliğin süre üzerinde değil, doğruluk üzerinde etkili olduğunu ispatlamıştır.[cite: 1]

## 🚀 Çalıştırma
Projeyi yerel bilgisayarınızda çalıştırmak için:
1. Python yüklü olduğundan emin olun.
2. Depoyu klonlayın veya dosyayı indirin.
3. Terminal üzerinden şu komutu çalıştırın:
   ```bash
   python odev.py
