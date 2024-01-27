from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)
model = joblib.load('finalized_model_joblib_kranti.sav')

@app.route('/api', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    prediction = model.predict([[data['sl'], data['sw'], data['pl'], data['pw']]])
    return jsonify(int(prediction[0]))

if __name__ == '__main__':
    app.run(port=8111, debug=True)
