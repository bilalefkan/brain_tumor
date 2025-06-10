import cv2
import numpy as np
from tensorflow.keras.models import load_model


model = load_model("beyin_tumoru_modeli.h5")


def predict_image(image_path, model, img_size=(224, 224)):
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, img_size)
    img = img / 255.0
    img = np.expand_dims(img, axis=0)  
    prediction = model.predict(img)
    if prediction[0][0] > 0.5:
        return "Beyin tümörü yok"
    else:
        return "Beyin tümörü var"


test_image = r"C:\Users\bilalefkan\Desktop\proje\test_image.jpg"
result = predict_image(test_image, model)
print(f"Sonuç: {result}")
