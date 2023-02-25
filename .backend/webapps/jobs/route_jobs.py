from fastapi import APIRouter
from fastapi import Request,Depends
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from db.repository.jobs import list_jobs
from db.session import get_db


# создали объект шаблона Jinja2 и связали его с папкой шаблонов
templates = Jinja2Templates(directory="templates")

# создали экземпляр объекта APIRouter, его надо добавить в main
# include_in_schema = False - исключаем маршрут из документации, т.к. это не API
router = APIRouter(include_in_schema=False)


@router.get("/")
async def home(request: Request,db: Session = Depends(get_db)):
    jobs = list_jobs(db=db)
    return templates.TemplateResponse(
        "general_pages/homepage.html", {"request": request,"jobs":jobs}
    )
