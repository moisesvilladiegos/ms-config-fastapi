from sqlalchemy.orm import Session

from src.app.rate.domain.models import rate
from src.app.rate.domain.schemas import rate_schema


def get_all(db):
    data = db.query(rate.Rate).all()
    return data

def get_by_id(id, db):
    data = db.query(rate.Rate).get(id)
    return data

# def save(schema: rate_schema.RateSchema, db: Session):
#     data = rate.Rate(id = schema.id, value = schema.value, parking_space_id = schema.parking_space_id)
#     db.add(data)
#     db.commit()
#     return schema

# def delete_v1(id, db: Session):
    
#     query = db.query(rate.Rate).filter(rate.ParkingSpace.id == id)
#     reponse_query = query.first()

#     if not reponse_query:
#         return f'No parking space with this id: {id} found'

#     query.delete(synchronize_session=False)
#     db.commit()
#     return id

# def put(id, item, db: Session):
    
#     query = db.query(rate.ParkingSpace).filter(rate.ParkingSpace.id == id)
#     reponse_query = query.first()

#     if not reponse_query:
#         return f'No parking space with this id: {id} found'

#     update_data = item.dict(exclude_unset=True)
#     query.filter(rate.ParkingSpace.id == id).update(update_data, synchronize_session=False)

#     db.commit()
#     db.refresh(reponse_query)
#     return {"status": "success", "rate": reponse_query}