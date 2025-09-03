from http.client import HTTPException
from typing import List



from fastapi import FastAPI
from pydantic import BaseModel
from starlette.requests import Request
from starlette.responses import Response, JSONResponse

app = FastAPI()



@app.get("/ping")
def hello():
    return Response(content="pong", status_code=200, media_type="text/plain")


# 2 a
class Characteristic(BaseModel):
    max_speed: float
    max_fuel_capacity: float

class Car(BaseModel):
    identifier: str
    brand: str
    model: str
    characteristics: Characteristic
cars_db = []

@app.post("/cars", status_code=201)
async def create_cars(cars: List[Car]):

    try:
        for car in cars:
            cars_db.append(car.dict())

        return {"message": f"Successfully created {len(cars)} car(s)", "cars": cars}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/cars")
async def get_cars():
    return cars_db


#  c

@app.post("/cars", status_code=201)
async def create_mob(cars: List[Car]):
    try:

        for car in cars:
            cars_db.append(car.dict())

        return {"message": f"Successfully created {len(cars)} car(s)", "cars": cars}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/cars")
async def get_cars():
    return cars_db

 # ----d
@app.get("/cars/{car_id}")
async def get_car(car_id: str):
    for car in cars_db:
        if car["identifier"] == car_id:
            return car
    raise HTTPException(
        status_code=404,
        detail=f"Car with id {car_id} does not exist or was not found"
    )


# e --bonus---
@app.put("/cars/{car_id}/characteristics", response_model=Car)
async def update_car_characteristics(car_id: str, characteristics: Characteristic):
    for car in cars_db:
        if car["identifier"] == car_id:
            car["characteristics"] = characteristics.dict()
            return car

    raise HTTPException(
        status_code=404,
        detail=f"Car with id {car_id} does not exist or was not found"
    )






