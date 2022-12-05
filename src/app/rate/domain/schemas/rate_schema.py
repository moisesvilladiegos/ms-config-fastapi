from pydantic import BaseModel

class RateSchema(BaseModel):
    id: int
    value: int
    parking_space_id: int

    class Config:
        orm_mode = True