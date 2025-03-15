import streamlit as st
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
        st.error(f"Ошибка при отправке POST-запроса: {e}")
        return None

# Интерфейс Streamlit
st.title("Streamlit приложение для предсказания модели")

# Ввод данных пользователем
input_data_str = st.text_input("Введите входные данные (через запятую):", "0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0")

# Преобразуем строку в список чисел
try:
    input_data = [float(x.strip()) for x in input_data_str.split(",")]
    if len(input_data) != 10:
        st.error("Пожалуйста, введите 10 чисел.")
except ValueError:
    st.error("Пожалуйста, введите корректные числа.")

# URL вашего сервера модели
server_url = "http://localhost:8000/v2/models/mobilenetv2_12/infer"

# Кнопка для отправки запроса
if st.button("Отправить запрос") and len(input_data) == 10:
    prediction = post_model_prediction(server_url, input_data)
    if prediction is not None:
        st.write("Предсказание модели:", prediction)