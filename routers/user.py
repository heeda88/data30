

from fastapi import APIRouter,Request, Response
from fastapi.templating import Jinja2Templates
from jose import jwt

from routers.auth import auth_token



router=APIRouter()
templates= Jinja2Templates(directory="static/templates")

@router.get("/")
def login_view(request:Request, msg: str=None,):
	data=auth_token(request=request)
	return templates.TemplateResponse(name="login.html",context={"request":request, "msg":msg, 'data':data})

@router.get("/home")
def home_view(request: Request, msg: str=None):
	data=auth_token(request=request)
	return templates.TemplateResponse(name="home.html",context={"request":request, "msg":msg, 'data':data})

@router.get("/admin")
def home_view(request: Request, msg: str=None):
	data=auth_token(request=request)
	return templates.TemplateResponse(name="admin.html",context={"request":request, "msg":msg, 'data':data})
