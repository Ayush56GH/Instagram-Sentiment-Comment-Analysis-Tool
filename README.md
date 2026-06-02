# Instagram Sentiment Analysis API 🚀

## 📌 Overview
This project is a Machine Learning-based **Sentiment Analysis System** built using **AutoGluon** and deployed using **FastAPI**.  

It predicts whether an Instagram comment is:
- Positive 😊
- Negative 😡
- Neutral 😐 (if applicable in dataset)

The model is trained on a dataset of **30,000 Instagram comments**.

---

## ⚙️ Tech Stack
- Python
- AutoGluon (AutoML)
- FastAPI
- Pandas
- Scikit-learn
- Uvicorn

---

## 📁 Project Structure

```
Sentiment Project/
│
├── main.py                 # FastAPI application
├── requirements.txt       # Dependencies
├── README.md              # Project documentation
├── .gitignore             # Ignored files
│
├── Predictor/             # Trained AutoGluon model (NOT pushed to GitHub if large)
│   ├── learner.pkl
│   ├── predictor.pkl
│   ├── models/
│   ├── utils/
│
├── data/                  # Dataset (optional)
├── notebooks/             # EDA + training notebooks
└── predictor.zip          # Backup model file (optional)
```

---

## 🚀 How It Works

1. User sends an Instagram comment
2. API processes text features:
   - clean_text
   - text_length
3. AutoGluon model predicts sentiment
4. Returns prediction + confidence score

---

## ▶️ Run Locally

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Start FastAPI server
```bash
uvicorn main:app --reload
```

### 3. Open API docs
```text
http://127.0.0.1:8000/docs
```

---

## 📡 API Endpoints

### 🔹 Home
```http
GET /
```

Response:
```json
{
  "message": "Instagram Sentiment API Running"
}
```

---

### 🔹 Predict Sentiment
```http
POST /predict
```

Request:
```json
{
  "comment": "This product is amazing"
}
```

Response:
```json
{
  "comment": "This product is amazing",
  "sentiment": "Positive",
  "confidence": {
    "Positive": 0.95,
    "Negative": 0.05
  }
}
```

---

## 🤖 Model Details

- Algorithm: AutoGluon TabularPredictor
- Training Data: 30,000 Instagram comments
- Features:
  - clean_text
  - text_length
- Output: Sentiment Class

---

## ☁️ Deployment (Azure) (In future) - In Process

This API can be deployed using:
- Azure App Service
- Azure Container Apps

Startup command:
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

---

## 📦 Model Note

The trained model (`Predictor/`) is not always included in GitHub because of large file size.

To run locally:
1. Download model ZIP
2. Extract as:
```
Predictor/
```
3. Place inside project root

---

## 📊 Future Improvements

- Streamlit UI dashboard
- Real-time Instagram scraping
- Sentiment trend analytics
- Tableau dashboard integration
- Multi-language sentiment detection

---

## 👨‍💻 Author
Ayush Kumar

---

## ⭐ If you like this project
Give a star ⭐ on the repository
