from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

model = joblib.load('model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json

    result = model.predict([[
        data['amount'],
        data['age'],
        data['previous claims'],
        data['vehicle_age'],
        data['policy_years']
        ]])

    return jsonify({
        "fraud_prediction": int(result[0])
        })

    app.run(host='0.0.0.0', port=5000)


