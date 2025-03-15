import requests
import numpy as np
from PIL import Image
import io

def preprocess_image(image_data):
    try:
        img = Image.open(io.BytesIO(image_data)).convert('RGB')
        img = img.resize((224, 224))
        img_array = np.array(img).astype('float32')  # Make sure this is float32
        img_array /= 255.0
        img_array = np.transpose(img_array, (2, 0, 1))
        img_array = np.expand_dims(img_array, axis=0)
        return img_array
    except Exception as e:
        print(f"Ошибка при обработке изображения: {e}")
        return None

# Read and preprocess the image
try:
    with open('lion.jpg', 'rb') as image_file:
        image_bytes = image_file.read()
        processed_image = preprocess_image(image_bytes)

        if processed_image is not None:
            # Ensure the numpy array is in float32 before converting to list
            processed_image = processed_image.astype('float32')  # Ensure dtype is float32

            # Convert numpy array into a flat list
            image_data = processed_image.flatten().tolist()  # Flatten before converting

            # Create the JSON request payload
            headers = {'Content-Type': 'application/json'}
            data = {'numbers': image_data}

            print("Data type before sending:", processed_image.dtype)  # This should print float32

            # Send the request
            response = requests.post('http://localhost:8000/predict', json=data, headers=headers)

            if response.status_code == 200:
                print("Получено предсказание:", response.json())
            else:
                print("Ошибка при отправке запроса:", response.text)
        else:
            print("Ошибка при обработке изображения")
except FileNotFoundError:
    print("Файл изображения не найден. Проверьте путь к файлу.")