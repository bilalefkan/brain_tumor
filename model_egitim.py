import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from sklearn.model_selection import train_test_split

# Veri yükleme (veri_yukleme.py'den X ve y'yi import edin)
from veri_yukleme import X, y

# Eğitim ve doğrulama setlerini ayırma
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

# Modeli oluşturma
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 3)),
    MaxPooling2D((2, 2)),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Flatten(),
    Dense(128, activation='relu'),
    Dense(1, activation='sigmoid') 
])


model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])


history = model.fit(X_train, y_train, epochs=10, validation_data=(X_val, y_val))


model.save("beyin_tumoru_modeli.h5")
print("Model kaydedildi!")

from tensorflow.keras.models import load_model


model_path = r"C:\Users\bilalefkan\Desktop\proje\beyin_tumoru_modeli.h5"
model = load_model(model_path)


model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
print("Model başarıyla derlendi!")
