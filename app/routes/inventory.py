from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/inventory", response_class=HTMLResponse)
async def get_inventory(request: Request):
    return templates.TemplateResponse("inventory.html", {"request": request})

@router.post("/inventory", response_class=HTMLResponse)
async def post_inventory(request: Request, category: str = Form(...), brand: str = Form(...),
                         condition: str = Form(...), warehouse: str = Form(...)):
    # Placeholder for handling form submission
    return templates.TemplateResponse("inventory.html", {
        "request": request,
        "message": f"Received: {category}, {brand}, {condition}, {warehouse}"
    })
