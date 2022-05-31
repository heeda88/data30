

from fastapi import APIRouter,Request, Response
from fastapi.templating import Jinja2Templates




router=APIRouter()
templates= Jinja2Templates(directory="static/templates")

@router.get("/myinfo")
def login_view(request:Request, msg: str=None,):
	return templates.TemplateResponse(name="myinfo.html",context={"request":request, "msg":msg})


@router.get("/item2")
def home_view(request: Request, msg: str=None):
	return templates.TemplateResponse(name='item2.html',context={"request":request, "msg":msg})