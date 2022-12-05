from sqlalchemy.orm import Session
from sqlalchemy import delete

from src.app.parking_space.domain.models import parking_space
from src.app.parking_space.domain.schemas import parking_space_schema

def get_all(db):
    data = db.query(parking_space.ParkingSpace).all()
    return data

def get_by_id(id, db):
    data = db.query(parking_space.ParkingSpace).get(id)
    return data

def save(schema: parking_space_schema.ParkingSpaceSchema, db: Session):
    data = parking_space.ParkingSpace(id = schema.id, type = schema.type, count = schema.count)
    db.add(data)
    db.commit()
    return schema

def delete_v1(id, db: Session):
    
    query = db.query(parking_space.ParkingSpace).filter(parking_space.ParkingSpace.id == id)
    reponse_query = query.first()

    if not reponse_query:
        return f'No parking space with this id: {id} found'

    query.delete(synchronize_session=False)
    db.commit()
    return id

def put(id, item, db: Session):
    
    query = db.query(parking_space.ParkingSpace).filter(parking_space.ParkingSpace.id == id)
    reponse_query = query.first()

    if not reponse_query:
        return f'No parking space with this id: {id} found'

    update_data = item.dict(exclude_unset=True)
    query.filter(parking_space.ParkingSpace.id == id).update(update_data, synchronize_session=False)

    db.commit()
    db.refresh(reponse_query)
    return {"status": "success", "parking_space": reponse_query}