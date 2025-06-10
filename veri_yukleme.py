import os
import cv2
import numpy as np


data_dir = r"C:\Users\bilalefkan\Desktop\proje\brian"
categories = ["tumor_var", "tumor_yok"]  


def load_images(data_dir, categories, img_size=(224, 224)):
    data = []
    for category in categories:
        path = os.path.join(data_dir, category)
        class_label = categories.index(category)  
        for img_name in os.listdir(path):
            try:
                img_path = os.path.join(path, img_name)
                img = cv2.imread(img_path)
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  
                img = cv2.resize(img, img_size)  
                data.append([img, class_label])
            except Exception as e:
                print(f"Bir hata oluştu: {e}")
    return data


data = load_images(data_dir, categories)
print(f"Toplam görüntü sayısı: {len(data)}")


import random
random.shuffle(data)


X = np.array([item[0] for item in data])  
y = np.array([item[1] for item in data])  

X = X / 255.0  

print(f"Görsellerin şekli: {X.shape}")
print(f"Etiketlerin şekli: {y.shape}")
