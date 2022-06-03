

from fastapi import APIRouter,Request, Response
from fastapi.templating import Jinja2Templates

from routers.auth import auth_token



router=APIRouter(tags=['user_view'])
templates= Jinja2Templates(directory="static/templates")

@router.get("/myinfo")
def login_view(request:Request, msg: str=None,):
	data =auth_token(request=request)
	return templates.TemplateResponse(name="myinfo.html",context={"request":request, "data":data})

