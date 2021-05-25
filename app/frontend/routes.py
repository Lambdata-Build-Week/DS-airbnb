from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


router = APIRouter()

templates = Jinja2Templates(directory="app/frontend/templates/")

@router.get('/', response_class=HTMLResponse)
def display_index(request: Request):
    return templates.TemplateResponse('index.html', {"request": request})


@router.get('/prediction', response_class=HTMLResponse)
def display_index(request: Request):
    return templates.TemplateResponse('prediction.html', {"request": request})


@router.get('/graph', response_class=HTMLResponse)
def display_index(request: Request):
    return templates.TemplateResponse('graph.html', {"request": request})