# app/routes/dish.py

from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from config.db import dishes_db
from models.plats import Dish
from schemas.plats_schemas import DishCreate, DishUpdate, DishResponse
from utils.auth_securite import oauth2_scheme

router = APIRouter()

@router.get("/plat", response_model=List[DishResponse])
async def get_dishes():
    return dishes_db

@router.get("/plats/{name}", response_model=DishResponse)
async def get_dish(name: str):
    dish = next((dish for dish in dishes_db if dish["name"] == name), None)
    if dish is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Dish not found")
    return dish

@router.post("/new_plat", response_model=DishResponse)
async def create_dish(dish: DishCreate, token: str = Depends(oauth2_scheme)):
    new_dish = dish.dict()
    dishes_db.append(new_dish)
    return new_dish

@router.put("/update_plat/{name}", response_model=DishResponse)
async def update_dish(name: str, dish: DishUpdate, token: str = Depends(oauth2_scheme)):
    existing_dish = next((d for d in dishes_db if d["name"] == name), None)
    if existing_dish is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Dish not found")
    existing_dish.update(dish.dict())
    return existing_dish

@router.delete("/delete_plat/{name}", response_model=dict)
async def delete_dish(name: str, token: str = Depends(oauth2_scheme)):
    global dishes_db
    dishes_db = [d for d in dishes_db if d["name"] != name]
    return {"message": "Dish deleted successfully"}
