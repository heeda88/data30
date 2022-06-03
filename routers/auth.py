


from fastapi import APIRouter,Request, Response
from fastapi.templating import Jinja2Templates
from jose import jwt


router=APIRouter()
templates= Jinja2Templates(directory="static/templates")


fake_db={'admin':{'email':'admin@namu.com','password':'namu02110','name':'관리자','role':'admin'
}}



def auth_token(request: Request):
	data ={}
	if 	'access_token' in request._cookies.keys() :
		token=request._cookies['access_token']
		data=jwt.decode(token,key="sort", algorithms='HS256')
		return data
	else :
		return data

def logout(request:Request):
	data ={}
	response = templates.TemplateResponse("login.html", {"request": request, "data":data})
	response.delete_cookie('access_token')
	return response

@router.get("/login")
async def login(request:Request):
	data=auth_token(request)
	return templates.TemplateResponse(name="login.html",context={"request":request,"data":data})

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

	# session 호출 

	# email 입력 예외처리 입력값없음
	if not email:
		errors.append("Please enter valid email")

	# password 입력 예외처리
	if len(password)<=4:
		errors.append("please enter valid password")

	# verify email
	if email!=fake_db['admin']['email']:
		errors.append("check your email & password")
	# verify email
	if password!=fake_db['admin']['password']:
		errors.append("check your email & password")

	if len(errors)==0:
		msg.append("Login successfully")
		data['email']=fake_db['admin']['email']
		data['name']=fake_db['admin']['name']
		data['role']=fake_db['admin']['role']	
		data['msg']=msg

		jwt_token= jwt.encode(claims=data,key="sort", algorithm='HS256')
		access_token=jwt_token
		response=templates.TemplateResponse(name="login.html",context={"request":request,"data":data})
		response.set_cookie(key="access_token", value=f"{access_token}", httponly=True)
		return response
	else :
		errors.append('login_failed')
		data['errors']=errors
		return templates.TemplateResponse(name="login.html",context={"request":request, "data":data})

@router.get("/logout")
def delete_cookie(request: Request):
	return logout(request=request)