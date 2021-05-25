"""Primary file for the creation and running of this Airbnb pricing web app."""

# For creating and running our web app with FastAPI
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import uvicorn

# For routing between front end, back end, and databse
from app.database import db
from app.ml_viz import ml, viz
from app.frontend import routes


# Instantiate fastAPI with appropriate descriptors
app = FastAPI(
    title='Airbnb Pricing API',
    description="Interactive pricing tool for Airbnb hosts",
    version="1.0",
    docs_url='/docs'
)


# Create access to static files on the page
app.mount("/assets",
          StaticFiles(directory="app/frontend/templates/assets"),
          name="assets"
          )

app.mount("/images",
          StaticFiles(directory="app/frontend/templates/images"),
          name="images"
          )


# Connect to the routing utilized in the other files of the app
app.include_router(routes.router, tags=['Frontend'])  # for routing user inputs
app.include_router(db.router, tags=['Database'])  # interactions with database
app.include_router(ml.router, tags=['Machine Learning'])  # predictive model
app.include_router(viz.router, tags=['Visualization'])  # interactive content


# Allow access between the front end and back end from different origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


if __name__ == '__main__':
    uvicorn.run(app)
