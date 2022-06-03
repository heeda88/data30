

from fastapi import APIRouter,Request, Response
from fastapi.templating import Jinja2Templates

from routers.auth import auth_token



router=APIRouter(tags=['item_view'])
templates= Jinja2Templates(directory="static/templates")

@router.get("/item1")
def login_view(request:Request, msg: str=None,):
	data =auth_token(request=request)
	return templates.TemplateResponse(name="item1.html",context={"request":request, "data":data})

@router.get("/item2")
def home_view(request: Request, msg: str=None):
	data =auth_token(request=request)
	return templates.TemplateResponse(name='item2.html',context={"request":request, "data":data})