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
    text = preprocess(input.text)
    prediction = rfc.predict(cv.transform([text]))
    return {"message":"success","is_suicide": int(prediction)}