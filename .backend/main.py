from fastapi import FastAPI
from core.config import settings
from apis.general_pages.route_homepage import general_pages_router

# функция подключения APIRouter
def include_router(app):
    app.include_router(general_pages_router)

# создание приложения и подключения APIRouter    
def start_application():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    include_router(app)
    return app
    
app = start_application()