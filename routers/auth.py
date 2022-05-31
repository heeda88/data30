


from fastapi import APIRouter,Request, Response
from fastapi.templating import Jinja2Templates
from jose import jwt


router=APIRouter()
templates= Jinja2Templates(directory="static/templates")

class  fakeDB:
	def __init__(self):
		self.email="example@example.com"
		self.password="example"

settings=fakeDB()


@router.get("/login")
async def login(request:Request):
	token=request._cookies['access_token']
	errors=[]
	data=jwt.decode(token,key="sort", algorithms='HS256')
	return templates.TemplateResponse(name="login.html",context={"request":request, "errors":errors, "email":data['email']})

@router.post("/login")
async def login(response:Response, request:Request):

	# auth True
	auth=True

	# gen err list
	msg=[]
	errors=[]
	data={}

	# get auth target
	form = await request.form()

	# get email
	email= form.get('email')

	# get password
	password=form.get("password")

	# email 입력 예외처리 입력값없음
	if not email:
		errors.append("Please enter valid email")

	# password 입력 예외처리
	if len(password)<=6:
		errors.append("please enter valid password")

	# verify email
	if email!=settings.email:
		auth=False

	# verify email
	if password!=settings.password:
		auth=False

	if auth:
		data['email']=email
		jwt_token= jwt.encode(claims=data,key="sort", algorithm='HS256')
		access_token=jwt_token
		print(access_token)
		response=templates.TemplateResponse(name="login.html",context={"request":request, "msg":msg, "email":email})
		response.set_cookie(key="access_token", value=f"{access_token}", httponly=True)
		return response
	else :
		errors.append('login_failed')
		return templates.TemplateResponse(name="login.html",context={"request":request, "errors":errors})


