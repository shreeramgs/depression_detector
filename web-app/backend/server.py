from fastapi import FastAPI
from pydantic import BaseModel
from preprocess import preprocess
from sklearn.feature_extraction.text import CountVectorizer
import joblib

class Input(BaseModel):
    text: str

app = FastAPI()
cv = joblib.load('cv.pkl')
rfc = joblib.load('rfc.pkl')

@app.get("/predict")
async def run_predict(input: Input):
    prediction = 0
    text = preprocess(input.text)
    probability = rfc.predict_proba(cv.transform([text]))
    if probability[0][1] > 0.3:
        prediction = 1
    return {"message":"success","is_suicide": prediction}