from flask import Flask, request, jsonify
from predict import Predict
from PIL import Image
import io
from flask_cors import CORS

predict = Predict('./model/weight.pth', './model/label_map.json', './model/language_map.json', './model/weight_is_animal.pth')


app = Flask(__name__)
CORS(app)

@app.route('/predict', methods=['POST'])
def classify():
    if 'file' not in request.files:
        return 'No file part', 400
    
    try:
        file = request.files['file']
        server = True
        if server:            
            import uuid
            _uuid = uuid.uuid1()
            filepath = f'/var/www/html/static/animal/{_uuid}.jpg'
            image_url = f"http://154.8.193.179:81/static/animal/{_uuid}.jpg"
        else:
            filepath = './model/image.jpg'
        file.save(filepath)
        img = Image.open(filepath).convert('RGB')
        # 将上传的图片文件转换为字节流
        # img_bytes = file.read()
        # img = Image.open(io.BytesIO(img_bytes)).convert('RGB')
    except:
        return 'error', 400
    
    use_api = True
    if use_api:
        import api
        prediction = api.predict(filepath)
        prediction['image_url'] = image_url
        print(prediction)
        return prediction
    else:
        prediction = predict.predict(image=img)
        prediction['image_url'] = image_url
        print(prediction)
        return jsonify({'prediction': prediction})
    



@app.route('/hello', methods=['GET'])
def hello():
    return 'hello'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)