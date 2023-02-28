from db.repository.jobs import list_jobs
from db.repository.jobs import retreive_job
from db.session import get_db
from fastapi import APIRouter
from fastapi import Depends
from fastapi import Request
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session


# создали объект шаблона Jinja2 и связали его с папкой шаблонов
templates = Jinja2Templates(directory="templates")

# создали экземпляр объекта APIRouter, его надо добавить в main
# include_in_schema = False - исключаем маршрут из документации, т.к. это не API
router = APIRouter(include_in_schema=False)


@router.get("/")
async def home(request: Request, db: Session = Depends(get_db), msg: str = None):
    jobs = list_jobs(db=db)
    return templates.TemplateResponse(
        "general_pages/homepage.html", {"request": request, "jobs": jobs, "msg": msg}
    )


@router.get("/details/{id}")
def job_detail(id: int, request: Request, db: Session = Depends(get_db)):
    job = retreive_job(id=id, db=db)
    return templates.TemplateResponse(
        "jobs/detail.html", {"request": request, "job": job}
    )
