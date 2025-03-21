**Проект по предмету Эксплуатация моделей машинного обучения**

[![Демонстрация работы (VK Video)](https://github.com/JuliaLapova/Telegram_Project/blob/main/mlops.jpg)](https://vkvideo.ru/video25188700_456239033)

Части проекта:
- Создана простая модель для предсказания числовых значений (код для сборки модели содержится в файле project.py)
- Модель экспортирована в ONNX с динамическими осями.
- Часть с TenzorRT пропущена по причине отсутствия GPU
- Настроен Triton Server (запускается из Docker контейнера)
- Создано приложение StreamLit - вебформа с возможностью отправки запроса и получения ответа от модели.


Запуск приложения:

- Запустить Docker
- В терминале активировать venv проекта
    ```.\venv\Scripts\activate```
- Запустить Triton Server, из виртуального окружения venv:  
    ```docker run --rm -p8000:8000 -p8001:8001 -p8002:8002 -v .\my_model:/models nvcr.io/nvidia/tritonserver:23.02-py3 tritonserver --model-repository=/models```
- После того как запущен Triton Server, в новом терминале можно запустить StreamLit app:
    ```C:\Users\Пользователь\Telegram_Project\venv\Scripts\python.exe -m streamlit run s_app.py```
- Перейти по адресу http://localhost:8501/
    Откроется страница, где нужно ввести 10 float значений
    После нажатия "Отправить запрос", на странице выведется информация в формате JSON, в которой будет значение вывода состоящее из 5 float значений.
