from typing import Optional

class Dish:
    def __init__(self, name: str, description: Optional[str], price: float):
        self.name = name
        self.description = description
        self.price = price