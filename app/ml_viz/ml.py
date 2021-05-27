"""Machine learning functions / price recommendation tool"""

# Import package to "unpickle" the predictive model
import joblib

# Import packages for routing / HTML support
from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates

# Import packages for predictive model and result dependencies
import pandas as pd
import numpy as np


# Instatiate the router
router = APIRouter()

# Instantiate templates
templates = Jinja2Templates(directory="app/frontend/templates/")

# Instatiate the predictive model
model = joblib.load("app/ml_viz/model.joblib")


# Setup the prediction process (how the data will be passed to the model)
def predict(
    property_type, room_type, accommodates, bathrooms, bedrooms, beds, city
        ):
    """Predict the best value for the Airbnb host's property based on
    specific features found in historical data.
    Parameters are the selected features of most importance (based on
    EDA and model testing).
    Returns a result in dollar amount.
    """

    # Pass the arguments into a dataframe to be passed into predictive model
    df = pd.DataFrame(columns=["property_type",
                               "room_type",
                               "accommodates",
                               "bathrooms",
                               "bedrooms",
                               "beds",
                               "city"
                               ],
                      data=[[property_type,
                             room_type,
                             accommodates,
                             bathrooms,
                             bedrooms,
                             beds,
                             city
                             ]]
                      )

    # Generate a prediction based on the information in the dataframe
    y_pred = model.predict(df)[0][0]

    # Revert prediction logarithmic values and round for cents
    result = np.round(np.exp(y_pred), 2)

    return f"${result} per night"


# Route the inputs from the HTML form into the predictive model
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
    included) and passes them into the predict function (used as a
    helper function).
    Parameters are the request (cleverly utilized by Minh Nuyen to
    pass into the response template) as well as values for the features
    necessary for the prediction, collested from the HTML form.
    Returns an HTML template supplied through Jinja which displays the
    recommended price per night as well as the selections made by the
    user (Airbnb host) to make the reccomendation.
    """

    # Make the prediction
    prediction = predict(property_type,
                         room_type,
                         accommodates,
                         bathrooms,
                         bedrooms,
                         beds,
                         city
                         )

    return templates.TemplateResponse('prediction.html',
                                      {"request": request,
                                       "prediction": prediction,  # modiy?
                                       "property_type": property_type,
                                       "room_type": f'Room type: {room_type}',
                                       "accommodates": \
                                       f'Accommodate: {accommodates}',
                                       "bathrooms": f'Bathroom: {bathrooms}',
                                       "bedrooms": f'Bedroom: {bedrooms}',
                                       "beds": f'Bed: {beds}',
                                       "city": f'City: {city}'
                                       })


# Route for display of the prediction page
@router.get('/prediction')
def display_index(request: Request):
    return templates.TemplateResponse('prediction.html', {"request": request})
