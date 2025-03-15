import requests
import json

def post_model_prediction(server_url, input_data):
    try:
        payload = {
            "inputs": [
                {
                    "name": "input",
                    "shape": [1, 10],  # Пример размерности
                    "datatype": "FP32",
                    "data": input_data
                }
            ]
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.post(server_url, json=payload, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при отправке POST-запроса: {e}")
        return None

if __name__ == "__main__":
    server_url = "http://localhost:8000/v2/models/mobilenetv2_12/infer"
    # input_data = [0.1] * 10  # Пример входных данных
    # Выводим значение input_data
    input_data = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    print("Входные данные:", input_data)
    prediction = post_model_prediction(server_url, input_data)
    if prediction is not None:
        print("Предсказание модели:", prediction)