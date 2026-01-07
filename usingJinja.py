from fastapi.responses import HTMLResponse
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
app8=FastAPI()
templates=Jinja2Templates(directory=".")
@app8.get("/hello",response_class=HTMLResponse)
async def hello(request:Request):
    return templates.TemplateResponse("hello.html",{"request":request})
