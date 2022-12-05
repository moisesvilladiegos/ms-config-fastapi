from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from src.app.config import data_base
from src.app.rate.application.service import rate_service
from src.app.rate.domain.schemas import rate_schema

router = APIRouter()

@router.get(
    "/rate",
    response_class=JSONResponse,
    status_code=200,
    responses={200: {"description": "Calculated"}},
)
def get_all(db:Session = Depends(data_base.get_db)):
    data = rate_service.get_all(db)
    return data

@router.get(
    "/rate/{id}",
    response_class=JSONResponse,
    status_code=200,
    responses={200: {"description": "Calculated"}},
)
def get_by_id(id, db:Session = Depends(data_base.get_db)):
    data = rate_service.get_by_id(id, db)
    return data

@router.post(
    "/rate",
    response_class=JSONResponse,
    status_code=200,
    responses={200: {"description": "Calculated"}},
)
def save(item: rate_schema.RateSchema, db:Session = Depends(data_base.get_db)):
    data = rate_service.save(item, db)
    return data

@router.delete(
    "/rate/{id}",
    response_class=JSONResponse,
    status_code=200,
    responses={200: {"description": "Calculated"}},
)
def delete(id, db:Session = Depends(data_base.get_db)):
    data = rate_service.delete(id, db)
    return data

@router.put(
    "/rate/{id}",
    response_class=JSONResponse,
    status_code=200,
    responses={200: {"description": "Calculated"}},
)
def put(id, item: rate_schema.RateSchema, db:Session = Depends(data_base.get_db)):
    data = rate_service.put(id, item, db)
    return data