from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
import json
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# Настройка Jinja2
templates = Jinja2Templates(directory="templates")


def format_request_data(request):
    request_data = {
        "HTTP Method": request.method,
        "URL": str(request.url),
        "Client IP": request.client.host,
        "Headers": {key.decode(): value.decode() for key, value in request.headers.raw},
        "Query Parameters": dict(request.query_params),
        "Path Parameters": dict(request.path_params)
    }
    return json.dumps(request_data, indent=4, ensure_ascii=False)

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    formatted_request = format_request_data(request)
    return templates.TemplateResponse("success.html", {"request": request, "request_data": formatted_request})
