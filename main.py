from fastapi import FastAPI
from pydantic import BaseModel
from starlette.requests import Request
from starlette.responses import Response, JSONResponse

app = FastAPI()



@app.get("/ping")
def hello():
    return Response(content="pong", status_code=200, media_type="application/json")