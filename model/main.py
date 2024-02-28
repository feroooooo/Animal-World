from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/classify')
def classify():
    data = request.get_json()
    prediction = 'tiger'
    return jsonify({'prediction': prediction})


if __name__ == '__main__':
    app.run()