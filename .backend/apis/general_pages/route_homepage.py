from fastapi import APIRouter
from fastapi import Request
from fastapi.templating import Jinja2Templates

# создали объект шаблона Jinja2 и связали его с папкой шаблонов
templates = Jinja2Templates(directory="templates")

# создали экземпляр объекта APIRouter, его надо добавить в main
general_pages_router = APIRouter()


# создали функцию обработки запроса главной страницы, которая возвращает шаблон и запрос в виде словаря
@general_pages_router.get("/")
async def home(request: Request):
    return templates.TemplateResponse(
        "general_pages/homepage.html", {"request": request}
    )
