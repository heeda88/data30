from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from routers import user,auth
from views import item_view, user_view
app= FastAPI(docs_url='/docs')

app.mount(path="/static",app=StaticFiles(directory="static"), name='static')

app.include_router(user.router)
app.include_router(auth.router)
app.include_router(item_view.router)
app.include_router(user_view.router)