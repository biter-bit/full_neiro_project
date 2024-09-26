from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
import json

app = FastAPI()

# Настройка Jinja2
templates = Jinja2Templates(directory="templates")


def safe_json_serializable(data):
    """Преобразует данные в JSON-сериализуемый формат."""
    if isinstance(data, (str, int, float, bool)) or data is None:
        return data
    elif isinstance(data, list):
        return [safe_json_serializable(item) for item in data]
    elif isinstance(data, dict):
        return {str(key): safe_json_serializable(value) for key, value in data.items()}
    return str(data)  # Преобразуем неподходящие типы в строку


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    # Получаем все атрибуты request в виде словаря
    request_data = vars(request)

    # Сериализуем объект в JSON с помощью функции безопасной сериализации
    request_data_safe = safe_json_serializable(request_data)
    request_data_json = json.dumps(request_data_safe, indent=2)

    return templates.TemplateResponse("success.html", {"request": request_data_json})
