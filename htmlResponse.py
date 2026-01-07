from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app7 = FastAPI()

@app7.get("/hello/")
async def hello():
    ret = """
        <html>
        <body>
        <h2>Hello World!</h2>
        </body>
        </html>
    """
    return HTMLResponse(content=ret)
