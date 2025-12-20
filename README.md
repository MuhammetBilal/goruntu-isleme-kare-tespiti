## 🛠️ Kullanılan Teknolojiler
* **Dil:** Python 3.x
* **Model:** YOLOv8 (Ultralytics)
* **Görüntü İşleme:** OpenCV
* **Veri Seti Yönetimi:** Roboflow & Custom Tools

## 🚀 Geliştirme Süreci ve Problem Çözümü

Bu proje sadece hazır bir modelin eğitilmesi değil, iteratif bir **iyileştirme sürecidir.**

### 1. Karşılaşılan Sorun: Yanlış Pozitifler (False Positives)
İlk model (v1), sadece kare çerçevenin olduğu veri setiyle eğitildi, yerdeki parke desenlerini ve kareye benzeyen nesneleri (terlik, telefon vb.) hedef olarak algılıyordu.
İkinci model (v2) farklı bir kare çerçeveyle ve arka planla eğitildi.
Üçüncü model (v3) kare çerçenin yanında negatif görüntü eğitimi yapıldı. Boş zemin, farklı nesnelerin yanında karenin ayrımı yapıldı.
Dördüncü model (v4) webcam açıldığında insanı ve arka planı negatif görüntü olarak sayması için eğitidi.
### 2. Çözüm: Hard Negative Mining & Aspect Ratio
Modelin zekasını artırmak için iki aşamalı bir çözüm uygulandı:
* **Negatif Görüntü Eğitimi:** Hedefin **olmadığı** ama hedefi andıran (terlik, karışık zemin) fotoğraflar veri setine "boş" (null) olarak eklendi. Modele "Bunlar hedef DEĞİLDİR" öğretildi.


### 📈 Model Evrimi
* **v1:** Temel tespit (Düşük başarı, zemin hataları).
* **v2:** Mavi bantlı hedefler eklendi.
* **v3:** "Terlik/Ayakkabı" gibi yanıltıcı nesnelerle negatif eğitim yapıldı.
* **v4:** Webcam açıldığında insanı ve diğer nesneleri kare olarak almaması için negatif eğitim yapıldı..

