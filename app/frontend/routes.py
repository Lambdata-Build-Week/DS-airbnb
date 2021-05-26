from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


router = APIRouter()

templates = Jinja2Templates(directory="app/frontend/templates/")

@router.get('/', response_class=HTMLResponse)
def display_index(request: Request):
    return templates.TemplateResponse('index.html', {"request": request})


# Route to display the prediction page
@router.get('/prediction', response_class=HTMLResponse)
def display_index(request: Request):
    return templates.TemplateResponse('prediction.html', {"request": request})

async def echo(city: str = Form(...),
               number_bed: int = Form(...),
               number_bedroom: int = Form(...),
               property_type: str = Form(...),
               number_bathrooms: int = Form(...),
               accomodates: int = Form(...)
               ):
    
    return {'city': city,
            'number_bed': number_bed,
            'number_bedroom': number_bedroom,
            'property_type': property_type,
            'number_bathrooms': number_bathrooms,
            'accomodates': accomodates
            }


@router.get('/visualizations', response_class=HTMLResponse)
def display_index(request: Request):
    return templates.TemplateResponse('graph.html', {"request": request})