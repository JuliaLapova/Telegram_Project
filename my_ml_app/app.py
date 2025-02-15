from flask import Flask, request, jsonify
import numpy as np
import onnxruntime as ort
from PIL import Image
import io

app = Flask(__name__)

# Загрузка ONNX-модели
model_path = 'mobilenetv2-12.onnx'
session = ort.InferenceSession(model_path)

def preprocess_image(image_data):
    # Open the image from byte data using PIL
    img = Image.open(io.BytesIO(image_data)).convert('RGB')
    
    # Resize the image to 224x224
    img = img.resize((224, 224))

    # Convert the image to a numpy array
    img_array = np.array(img).astype('float32')

    # Normalize the image data to 0-1
    img_array /= 255.0

    # Transpose the dimensions (HWC to CHW)
    img_array = np.transpose(img_array, (2, 0, 1))

    # Add a batch dimension
    img_array = np.expand_dims(img_array, axis=0)

    return img_array

@app.route('/sum', methods=['POST'])
def calculate_sum():
    data = request.json
    if not data or 'numbers' not in data:
        return jsonify({"error": "Please provide 'numbers' array in JSON"}), 400
    
    try:
        array = np.array(data['numbers'])
        result = array.sum()
        # Преобразуем результат в стандартный тип данных Python (int)
        result = int(result)
        return jsonify({"sum": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    if not data or 'numbers' not in data:
        return jsonify({"error": "Please provide 'numbers' array in JSON"}), 400
    
    try:
        # Preprocess the image
        input_data = np.array(data['numbers'])
        
        # Get the input name for the model
        input_name = session.get_inputs()[0].name

        # Run the model
        result = session.run(None, {input_name: input_data})
        
        # Преобразуем результат в стандартный тип данных Python (list)
        result = result[0].tolist()
        return jsonify({"prediction": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)