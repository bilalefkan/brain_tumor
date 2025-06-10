Beyin Tümörü Tespiti - README
🧠 Beyin Tümörü Tespiti (Basit CNN Modeli)

📌 Projenin Amacı

Bu proje, basitleştirilmiş bir derin öğrenme modeli (Convolutional Neural Network - CNN) kullanarak beyin tümörü olup olmadığını sınıflandırmayı amaçlamaktadır. Görüntü verileriyle çalışarak, kullanıcıdan alınan bir MRI görüntüsünü analiz eder ve tümör varlığına dair tahmin üretir.

📂 Veri Seti

Veri seti şu adresten temin edilebilir:  
https://www.kaggle.com/datasets/preetviradiya/brian-tumor-dataset

Veri setini indirdikten sonra:

1. ZIP dosyasını masaüstüne çıkarın.
2. Çıkan klasörler genelde “Brain Tumor” ve “Healty” olarak isimlendirilmiştir.
3. Bu iki klasörü projeye `brian` isimli bir ana klasör altında yerleştirin.
4. `Brain Tumor` klasörünün adını `tumor_var`, `Healty` klasörünün adını ise `tumor_yok` olarak değiştirin.

📁 Dosya yapınız şu şekilde olmalı:

brain_tumor/
│
├── brian/
│   ├── tumor_var/
│   └── tumor_yok/
├── model_egitim.py
├── tahmin.py
├── veri_yukleme.py
├── test_image.jpg
├── beyin_tumoru_modeli.h5
└── README.md

📦 Gerekli Kütüphaneler

Projeyi çalıştırmadan önce aşağıdaki kütüphanelerin yüklü olduğundan emin olun:

pip install tensorflow scikit-learn opencv-python numpy

Kütüphaneler şunlar için kullanılmaktadır:

- tensorflow: CNN modelinin kurulumu, eğitimi ve tahmini
- scikit-learn: Eğitim ve test verisinin ayrılması
- opencv-python: Görüntü işleme (resim okuma ve yeniden boyutlandırma)
- numpy: Sayısal işlemler ve veri yapıları

⚠️ Not

Bu proje, daha karmaşık ve büyük ölçekli medikal görüntüleme projelerinin basitleştirilmiş bir örneğidir. Eğitim amacıyla geliştirilmiştir.
