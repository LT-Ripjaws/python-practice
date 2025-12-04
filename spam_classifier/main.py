from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import pickle

app = FastAPI()

with open("spam_classifier.pkl", "rb") as f:
    model = pickle.load(f)

class TextData(BaseModel):
    text: str

@app.post("/predict")
def predict(data: TextData):
    user_text = data.text
    pred = model.predict([user_text])[0]
    pred_label = "spam" if pred == 1 else "not spam"
    return {"prediction": pred_label}


@app.get("/", response_class=HTMLResponse)
def home():
    with open("index.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content)

# To run the app, type 'uvicorn main:app --reload' in the terminal and make sure you are inside the correct folder structure.