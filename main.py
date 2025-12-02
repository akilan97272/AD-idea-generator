from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from llm import generate_script, extract_visual_hook

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request,
        "script": None,
        "visual_hook": None
    })


@app.post("/generate", response_class=HTMLResponse)
def generate(
    request: Request,
    product_name: str = Form(...),
    target_audience: str = Form(...),
    tone: str = Form(...)
):
    script_text = generate_script(product_name, target_audience, tone)
    visual_hook = extract_visual_hook(script_text)

    return templates.TemplateResponse("index.html", {
        "request": request,
        "script": script_text,
        "visual_hook": visual_hook
    })
