import onnxruntime as ort



def print_model_input_info(model_path):
    # Создание сессии ONNX Runtime
    session = ort.InferenceSession(model_path)

    # Получение информации о входах модели
    print("Информация о входах модели:")
    for input in session.get_inputs():
        print(f"Имя: {input.name}")
        print(f"Форма: {input.shape}")
        print(f"Тип: {input.type}")

if __name__ == "__main__":
    model_path = "my_model/mobilenetv2_12/1/model.onnx"  # Замените на путь к вашей модели
    print_model_input_info(model_path)