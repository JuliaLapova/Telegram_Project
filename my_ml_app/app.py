from flask import Flask, request, jsonify
import numpy as np

app = Flask(__name__)

@app.route('/sum', methods=['POST'])
def calculate_sum():
    data = request.json
    if not data or 'numbers' not in data:
        return jsonify({"error": "Please provide 'numbers' array in JSON"}), 400
    
    try:
        array = np.array(data['numbers'])
        result = array.sum()
        return jsonify({"sum": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)