from pydantic import BaseModel

from pydantic_extra_types.coordinate import Coordinate


class Transaction(BaseModel):
    user: str
    text: str
    location: Coordinate


