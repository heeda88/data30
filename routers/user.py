

from fastapi import APIRouter,Request, Response
from fastapi.templating import Jinja2Templates




router=APIRouter()
templates= Jinja2Templates(directory="static/templates")

@router.get("/")
def login_view(request:Request, msg: str=None,):
	return templates.TemplateResponse(name="login.html",context={"request":request, "msg":msg})



@router.get("/home")
def home_view(request: Request, msg: str=None):
	return templates.TemplateResponse(name='home.html',context={"request":request, "msg":msg})