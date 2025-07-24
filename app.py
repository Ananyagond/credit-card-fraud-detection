from flask import Flask, render_template, request
import pandas as pd
import joblib
import os

# ✅ Initialize Flask app
app = Flask(__name__)
app.secret_key = 'your_secret_key'

# ✅ File upload folder
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# ✅ Load Model and Scaler
model = joblib.load('fraud_detection_model.pkl')
scaler = joblib.load('scaler.pkl')

# ✅ Routes (AFTER app initialization)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload_single', methods=['POST'])
def upload_single():
    file = request.files['single_csv']
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    df = pd.read_csv(filepath, header=None)
    if df.shape[1] != 30 or len(df) != 1:
        return render_template('index.html', single_result="❌ CSV must have 1 row & 30 columns")

    scaled_data = scaler.transform(df.values)
    prediction = model.predict(scaled_data)[0]
    probability = model.predict_proba(scaled_data)[0][1] * 100

    result = "⚠️ Fraudulent Transaction" if prediction == 1 else "✅ Legitimate Transaction"
    result += f" (Risk: {probability:.2f}%)"

    return render_template('index.html', single_result=result)

@app.route('/upload_batch', methods=['POST'])
def upload_batch():
    file = request.files['batch_csv']
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    df = pd.read_csv(filepath, header=None)
    if df.shape[1] != 30:
        return render_template('index.html', batch_result="❌ CSV must have 30 columns")

    scaled_data = scaler.transform(df.values)
    predictions = model.predict(scaled_data)
    probabilities = model.predict_proba(scaled_data)[:, 1]

    df['Prediction'] = ['Fraud' if p == 1 else 'Legit' for p in predictions]
    df['Probability (%)'] = (probabilities * 100).round(2)

    table_html = df[['Prediction', 'Probability (%)']].to_html(classes='table table-bordered table-striped', index=False)
    return render_template('index.html', batch_result=table_html)

if __name__ == '__main__':
    app.run(debug=True)
