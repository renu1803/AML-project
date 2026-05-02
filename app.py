from flask import Flask, render_template, request
import joblib
import numpy as np
import os

app = Flask(__name__)

# Load model
model = joblib.load(os.path.join("saved models", "Random_Forest.joblib"))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Example: assume 4 input features
        features = [float(x) for x in request.form.values()]
        final_features = np.array([features])

        prediction = model.predict(final_features)

        return render_template(
            'index.html',
            prediction_text=f"Prediction: {prediction[0]}"
        )
    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {e}")

if __name__ == "__main__":
    app.run(debug=True)
