from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
import json

app = FastAPI()

# Настройка Jinja2
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    # Получаем все атрибуты request в виде словаря
    request_data = vars(request)

    # Сериализуем объект в JSON
    request_data_json = json.dumps(request_data, default=str, indent=2)
    return templates.TemplateResponse("success.html", {"request": request_data_json})
