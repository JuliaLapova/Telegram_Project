import io
import requests
import numpy as np
from PIL import Image

def preprocess_image(image_data):
    """
    Предварительная обработка изображения из байтовых данных.

    Args:
        image_data: Байтовые данные изображения.

    Returns:
        NumPy массив, представляющий предварительно обработанное изображение.
        Возвращает None в случае ошибки.
    """
    try:
        # Открываем изображение из байтовых данных с помощью PIL
        img = Image.open(io.BytesIO(image_data)).convert('RGB')

        # Изменяем размер изображения до 224x224
        img = img.resize((224, 224))

        # Преобразуем изображение в массив NumPy
        img_array = np.array(img).astype('float32')

        # Нормализуем данные изображения до 0-1
        img_array /= 255.0

        # Транспонируем измерения (HWC в CHW)
        img_array = np.transpose(img_array, (2, 0, 1))

        # Добавляем измерение batch
        img_array = np.expand_dims(img_array, axis=0)

        return img_array
    except Exception as e:
        print(f"Ошибка при обработке изображения: {e}")
        return None


def send_image_to_server(image_path):
    """
    Отправляет изображение на сервер после предварительной обработки.
    """
    try:
        with open(image_path, "rb") as f:
            image_bytes = f.read()
        input_data = preprocess_image(image_bytes)
        if input_data is None:
            return  # Обработка ошибки в preprocess_image

        # Преобразуем в формат, подходящий для JSON (например, список списков)
        # Это может потребовать дополнительной обработки в зависимости от ожидаемого формата
        # В этом примере мы будем использовать упрощенное представление
        input_data_list = input_data.tolist()

        # Отправляем POST запрос
        response = requests.post('http://localhost/predict', json={'image': input_data_list})
        response.raise_for_status()  # Проверка кода ответа (200 OK)

        # Обработка ответа от сервера
        print(f"Ответ от сервера: {response.json()}")

    except FileNotFoundError:
        print(f"Ошибка: Изображение не найдено по пути: {image_path}")
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при отправке запроса: {e}")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")


if __name__ == "__main__":
    image_path = "lion.jpg"  # Замените на путь к вашему изображению
    send_image_to_server(image_path)