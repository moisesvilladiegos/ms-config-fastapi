from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from src.app.config import data_base
from src.app.parking_space.application.service import parking_space_service
from src.app.parking_space.domain.schemas import parking_space_schema

router = APIRouter()

@router.get(
    "/parking-space",
    response_class=JSONResponse,
    status_code=200,
    responses={200: {"description": "Calculated"}},
)
def get_all(db:Session = Depends(data_base.get_db)):
    data = parking_space_service.get_all(db)
    return data

@router.get(
    "/parking-space/{id}",
    response_class=JSONResponse,
    status_code=200,
    responses={200: {"description": "Calculated"}},
)
def get_by_id(id, db:Session = Depends(data_base.get_db)):
    data = parking_space_service.get_by_id(id, db)
    return data

@router.post(
    "/parking-space",
    response_class=JSONResponse,
    status_code=200,
    responses={200: {"description": "Calculated"}},
)
def save(item: parking_space_schema.ParkingSpaceSchema, db:Session = Depends(data_base.get_db)):
    data = parking_space_service.save(item, db)
    return data

@router.delete(
    "/parking-space/{id}",
    response_class=JSONResponse,
    status_code=200,
    responses={200: {"description": "Calculated"}},
)
def delete(id, db:Session = Depends(data_base.get_db)):
    data = parking_space_service.delete(id, db)
    return data

@router.put(
    "/parking-space/{id}",
    response_class=JSONResponse,
    status_code=200,
    responses={200: {"description": "Calculated"}},
)
def put(id, item: parking_space_schema.ParkingSpaceSchema, db:Session = Depends(data_base.get_db)):
    data = parking_space_service.put(id, item, db)
    return data