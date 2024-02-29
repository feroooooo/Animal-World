from flask import Flask, request, jsonify
from predict import Predict
from PIL import Image
import io
from flask_cors import CORS

predict = Predict('./model/weight.pth', './model/label_map.json')


app = Flask(__name__)
CORS(app)

@app.route('/predict', methods=['POST'])
def classify():
    if 'file' not in request.files:
        return 'No file part', 400
    
    file = request.files['file']
    # 将上传的图片文件转换为字节流
    img_bytes = file.read()
    img = Image.open(io.BytesIO(img_bytes)).convert('RGB')

    prediction = predict.predict(image=img)
    return jsonify({'prediction': prediction})


@app.route('/hello', methods=['GET'])
def hello():
    return 'hello'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)