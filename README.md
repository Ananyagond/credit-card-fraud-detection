# Credit Card Fraud Detection (Flask + ML + Docker)

## 📌 Overview
Detect fraudulent credit card transactions using **Machine Learning (Random Forest)** with a Flask-based web app.  
Features:
- ✅ Single & Batch CSV upload for prediction
- ✅ Dark Mode UI
- ✅ Dockerized for easy deployment

---

## 📊 Dataset
Download the dataset from Kaggle:  
👉 [Credit Card Fraud Detection Dataset](https://www.kaggle.com/mlg-ulb/creditcardfraud)

Place `creditcard.csv` in the project folder for local training.

---

## 🛠 Tech Stack
- **Backend:** Flask, Python
- **ML:** Scikit-learn
- **Frontend:** HTML, Bootstrap
- **Deployment:** Render, Railway, Docker

---

## ⚙️ Run Locally
```bash
git clone https://github.com/<your-username>/credit-card-fraud-detection.git
cd credit-card-fraud-detection

python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
pip install -r requirements.txt

python app.py

