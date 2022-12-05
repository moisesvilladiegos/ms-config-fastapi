from pydantic import BaseModel

class ParkingSpaceSchema(BaseModel):
    id: int
    type: str
    count: int

    class Config:
        orm_mode = True