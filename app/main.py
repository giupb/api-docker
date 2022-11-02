from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="app/templates")

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home(request: Request, c=False):
    return templates.TemplateResponse("index.html", {"request": request, "c":c})

@app.get("/new", response_class=HTMLResponse)
def new_home(request: Request, c=True):
    return templates.TemplateResponse("index.html", {"request": request, "c":c})