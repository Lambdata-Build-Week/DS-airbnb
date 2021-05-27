"""Machine learning functions"""

# import logging
import joblib

from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
import pandas as pd
import numpy as np
from pydantic import BaseModel, Field, validator

# log = logging.getLogger(__name__)
router = APIRouter()

templates = Jinja2Templates(directory="app/frontend/templates/")

model = joblib.load("app/ml_viz/model.joblib")


# class Item(BaseModel):
#     """Use this data model to parse the request body JSON."""

#     x1: float = Field(..., example=3.14)
#     x2: int = Field(..., example=-42)
#     x3: str = Field(..., example='banjo')

#     def to_df(self):
#         """Convert pydantic object to pandas dataframe with 1 row."""
#         return pd.DataFrame([dict(self)])

#     @validator('x1')
#     def x1_must_be_positive(cls, value):
#         """Validate that x1 is a positive number."""
#         assert value > 0, f'x1 == {value}, must be > 0'
#         return value


def predict(property_type, room_type, accommodates, bathrooms, bedrooms, beds, city):
    df = pd.DataFrame(columns=["property_type", "room_type", "accommodates", "bathrooms", "bedrooms", "beds", "city"],
    data=[[property_type, room_type, accommodates, bathrooms, bedrooms, beds, city]])
    y_pred = model.predict(df)[0][0]
    result = np.exp(y_pred)
    return np.round(result, 2)

# @router.get('/prediction', response_class=HTMLResponse)
@router.post('/prediction')
def echo(
    request: Request, 
    city: str=Form(...),
    beds: int=Form(...),
    bedrooms: int=Form(...),
    bathrooms: int=Form(...),
    accommodates: int=Form(...),
    property_type: str=Form(...),
    room_type: str=Form(...)
    ):
    """Gets the input data from predict.html (with respective dtypes
    included) and returns them in JSON format."""
    prediction = predict(property_type, room_type, accommodates, bathrooms, bedrooms, beds, city)
    return templates.TemplateResponse('prediction.html', {"request": request, "prediction": prediction,"property_type": property_type, "room_type": room_type, "accommodates": accommodates, "bathrooms": bathrooms, "bedrooms": bedrooms, "beds": beds, "city": city})

@router.get('/prediction')
def display_index(request: Request):
    return templates.TemplateResponse('prediction.html', {"request": request})


# @router.post('/prediction')
# async def predict(property_type, room_type, accommodates, bathrooms, bedrooms, beds, city):
#     df = pd.DataFrame(columns=["property_type", "room_type", "accommodates", "bathrooms", "bedrooms", "beds", "city"],
#     data=[[property_type, room_type, accommodates, bathrooms, bedrooms, beds, city]])
#     y_pred = model.predict(df)[0][0]
#     result = np.exp(y_pred)
#     return np.round(result, 2)

# def display_index(request: Request, prediction=predict("Apartment", "Private room", 5, 2, 3, 3, "Austin")):
#     return templates.TemplateResponse('prediction.html', {"request": request, "prediction": prediction})
