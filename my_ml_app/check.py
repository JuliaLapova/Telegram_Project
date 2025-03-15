import onnxruntime as ort

def check_onnx_model_in_docker(model_path):
    # Создание сессии ONNX Runtime
    session = ort.InferenceSession(model_path)

    # Получение информации о входах модели
    input_details = session.get_inputs()
    for input_detail in input_details:
        print(f"Входное имя: {input_detail.name}")
        print(f"Форма входа: {input_detail.shape}")
        print(f"Тип входа: {input_detail.type}")

    # Получение информации о выходах модели
    output_details = session.get_outputs()
    for output_detail in output_details:
        print(f"Выходное имя: {output_detail.name}")
        print(f"Форма выхода: {output_detail.shape}")
        print(f"Тип выхода: {output_detail.type}")

    print("Модель ONNX загружена и готова к использованию.")

if __name__ == "__main__":