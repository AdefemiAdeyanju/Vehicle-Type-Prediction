from fastapi import FastAPI
from pydantic import BaseModel
import pickle

app = FastAPI()

model = pickle.load(open('car_data.pkl', 'rb'))

class carinput(BaseModel):
    name: str
    model_year: int
    acceleration: int
    
    class caroutput(BaseModel):
        origin: str
        
@app.post('/predict/')
def predict_car_origin_prediction(input_data = carinput):
    