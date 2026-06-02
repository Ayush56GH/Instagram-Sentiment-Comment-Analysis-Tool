from fastapi import FastAPI
from pydantic import BaseModel
from autogluon.tabular import TabularPredictor
import pandas as pd

app = FastAPI(
    title="Instagram Sentiment API"
)

predictor = TabularPredictor.load("predictor")


class CommentRequest(BaseModel):
    comment: str


@app.get("/")
def home():
    return {"message": "Instagram Sentiment API Running"}


@app.post("/predict")
def predict_sentiment(data: CommentRequest):

    df = pd.DataFrame({
        "clean_text": [data.comment],
        "text_length": [len(data.comment)]
    })

    prediction = predictor.predict(df)
    probabilities = predictor.predict_proba(df)

    return {
        "comment": data.comment,
        "sentiment": str(prediction.iloc[0]),
        "confidence": probabilities.iloc[0].to_dict()
    }