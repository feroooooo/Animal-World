from flask import Flask, request, jsonify
from predict import Predict

predict = Predict('checkpoint/best_epoch30.pth', './model/label_map.json')


app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def classify():
    data = request.get_json()
    prediction = predict.predict("C:/Custom/DataSet/WildLife/cheetah/00000000_224resized.png")
    return jsonify({'prediction': prediction})


if __name__ == '__main__':
    app.run(port=5000)