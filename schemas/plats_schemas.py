from pydantic import BaseModel

class DishBase(BaseModel):
    name: str
    description: str
    price: float

class DishCreate(DishBase):
    pass

class DishUpdate(DishBase):
    pass

class DishResponse(DishBase):
    pass